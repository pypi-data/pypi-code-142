#
# libvirtaio -- asyncio adapter for libvirt
# Copyright (C) 2017  Wojtek Porczyk <woju@invisiblethingslab.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, see
# <http://www.gnu.org/licenses/>.
#

'''Libvirt event loop implementation using asyncio

Register the implementation of default loop:

    import asyncio
    import libvirtaio

    async def myapp():
      libvirtaio.virEventRegisterAsyncIOImpl()

      conn = libvirt.open("test:///default")

For compatibility with Python < 3.7:

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(myapp())

    asyncio.set_event_loop(None)
    loop.close()

If Python >= 3.7 can be required then

    asyncio.run(myapp())

.. seealso::
    https://libvirt.org/html/libvirt-libvirt-event.html
'''

import asyncio
import itertools
import logging
import warnings

import libvirt

from typing import Any, Callable, Dict, Generator, Optional, TypeVar  # noqa F401
_T = TypeVar('_T')

__author__ = 'Wojtek Porczyk <woju@invisiblethingslab.com>'
__license__ = 'LGPL-2.1+'
__all__ = [
    'getCurrentImpl',
    'virEventAsyncIOImpl',
    'virEventRegisterAsyncIOImpl',
]


class Callback(object):
    '''Base class for holding callback

    :param virEventAsyncIOImpl impl: the implementation in which we run
    :param cb: the callback itself
    :param opaque: the opaque tuple passed by libvirt
    '''
    # pylint: disable=too-few-public-methods

    _iden_counter = itertools.count()

    def __init__(self, impl: "virEventAsyncIOImpl", cb: Callable[[int, _T], None], opaque: _T, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)  # type: ignore
        self.iden = next(self._iden_counter)
        self.impl = impl
        self.cb = cb
        self.opaque = opaque

    def __repr__(self) -> str:
        return '<{} iden={}>'.format(self.__class__.__name__, self.iden)

    def close(self) -> None:
        '''Schedule *ff* callback'''
        self.impl.log.debug('callback %d close(), scheduling ff', self.iden)
        self.impl.schedule_ff_callback(self.iden, self.opaque)


#
# file descriptors
#

class Descriptor(object):
    '''Manager of one file descriptor

    :param virEventAsyncIOImpl impl: the implementation in which we run
    :param int fd: the file descriptor
    '''
    def __init__(self, impl: "virEventAsyncIOImpl", fd: int) -> None:
        self.impl = impl
        self.fd = fd
        self.callbacks = {}  # type: Dict

    def _handle(self, event: int) -> None:
        '''Dispatch the event to the descriptors

        :param int event: The event (from libvirt's constants) being dispatched
        '''
        for callback in list(self.callbacks.values()):
            if callback.event is not None and callback.event & event:
                callback.cb(callback.iden, self.fd, event, callback.opaque)

    def update(self) -> None:
        '''Register or unregister callbacks at event loop

        This should be called after change of any ``.event`` in callbacks.
        '''
        # It seems like loop.add_{reader,writer} can be run multiple times
        # and will still register the callback only once. Likewise,
        # remove_{reader,writer} may be run even if the reader/writer
        # is not registered (and will just return False).

        # For the edge case of empty callbacks, any() returns False.
        if any(callback.event & ~(
            libvirt.VIR_EVENT_HANDLE_READABLE |
            libvirt.VIR_EVENT_HANDLE_WRITABLE)
                for callback in self.callbacks.values()):
            warnings.warn(
                'The only event supported are VIR_EVENT_HANDLE_READABLE '
                'and VIR_EVENT_HANDLE_WRITABLE',
                UserWarning)

        if any(callback.event & libvirt.VIR_EVENT_HANDLE_READABLE
                for callback in self.callbacks.values()):
            self.impl.loop.add_reader(
                self.fd, self._handle, libvirt.VIR_EVENT_HANDLE_READABLE)
        else:
            self.impl.loop.remove_reader(self.fd)

        if any(callback.event & libvirt.VIR_EVENT_HANDLE_WRITABLE
                for callback in self.callbacks.values()):
            self.impl.loop.add_writer(
                self.fd, self._handle, libvirt.VIR_EVENT_HANDLE_WRITABLE)
        else:
            self.impl.loop.remove_writer(self.fd)

    def add_handle(self, callback: "FDCallback") -> None:
        '''Add a callback to the descriptor

        :param FDCallback callback: the callback to add
        :rtype: None

        After adding the callback, it is immediately watched.
        '''
        self.callbacks[callback.iden] = callback
        self.update()

    def remove_handle(self, iden: int) -> None:
        '''Remove a callback from the descriptor

        :param int iden: the identifier of the callback
        :returns: the callback
        :rtype: FDCallback

        After removing the callback, the descriptor may be unwatched, if there
        are no more handles for it.
        '''
        callback = self.callbacks.pop(iden)
        self.update()
        return callback


class DescriptorDict(dict):
    '''Descriptors collection

    This is used internally by virEventAsyncIOImpl to hold descriptors.
    '''
    def __init__(self, impl: "virEventAsyncIOImpl") -> None:
        super().__init__()
        self.impl = impl

    def __missing__(self, fd: int) -> Descriptor:
        descriptor = Descriptor(self.impl, fd)
        self[fd] = descriptor
        return descriptor


class FDCallback(Callback):
    '''Callback for file descriptor (watcher)

    :param Descriptor descriptor: the descriptor manager
    :param int event: bitset of events on which to fire the callback
    '''
    # pylint: disable=too-few-public-methods

    def __init__(self, *args: Any, descriptor: Descriptor, event: int, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.descriptor = descriptor
        self.event = event

    def __repr__(self) -> str:
        return '<{} iden={} fd={} event={}>'.format(
            self.__class__.__name__, self.iden, self.descriptor.fd, self.event)

    def update(self, event: int) -> None:
        '''Update the callback and fix descriptor's watchers'''
        self.event = event
        self.descriptor.update()


#
# timeouts
#

class TimeoutCallback(Callback):
    '''Callback for timer'''
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.timeout = -1
        self._task = None

    def __repr__(self) -> str:
        return '<{} iden={} timeout={}>'.format(
            self.__class__.__name__, self.iden, self.timeout)

    async def _timer(self) -> Generator[Any, None, None]:
        '''An actual timer running on the event loop.

        This is a coroutine.
        '''
        while True:
            try:
                if self.timeout > 0:
                    timeout = self.timeout * 1e-3
                    self.impl.log.debug('sleeping %r', timeout)
                    await asyncio.sleep(timeout)
                else:
                    # scheduling timeout for next loop iteration
                    await asyncio.sleep(0)

            except asyncio.CancelledError:
                self.impl.log.debug('timer %d cancelled', self.iden)
                break

            self.cb(self.iden, self.opaque)
            self.impl.log.debug('timer %r callback ended', self.iden)

    def update(self, timeout: int) -> None:
        '''Start or the timer, possibly updating timeout'''
        self.timeout = timeout

        if self.timeout >= 0 and self._task is None:
            self.impl.log.debug('timer %r start', self.iden)
            self._task = asyncio.ensure_future(self._timer(),
                                               loop=self.impl.loop)

        elif self.timeout < 0 and self._task is not None:
            self.impl.log.debug('timer %r stop', self.iden)
            self._task.cancel()  # pylint: disable=no-member
            self._task = None

    def close(self) -> None:
        '''Stop the timer and call ff callback'''
        self.update(timeout=-1)
        super(TimeoutCallback, self).close()


#
# main implementation
#

class virEventAsyncIOImpl(object):
    '''Libvirt event adapter to asyncio.

    :param loop: asyncio's event loop

    If *loop* is not specified, the current (or default) event loop is used.
    '''

    def __init__(self, loop: asyncio.AbstractEventLoop = None) -> None:
        self.loop = loop or asyncio.get_event_loop()
        self.callbacks = {}  # type: Dict[int, Callback]
        self.descriptors = DescriptorDict(self)
        self.log = logging.getLogger(self.__class__.__name__)

        self._pending = 0
        # Transient asyncio.Event instance dynamically created
        # and destroyed by drain()
        # NOTE invariant: _finished.is_set() iff _pending == 0
        self._finished = None

    def __repr__(self) -> str:
        return '<{} callbacks={} descriptors={}>'.format(
            type(self).__name__, self.callbacks, self.descriptors)

    def _pending_inc(self) -> None:
        '''Increase the count of pending affairs. Do not use directly.'''
        self._pending += 1
        if self._finished is not None:
            self._finished.clear()

    def _pending_dec(self) -> None:
        '''Decrease the count of pending affairs. Do not use directly.'''
        assert self._pending > 0
        self._pending -= 1
        if self._pending == 0 and self._finished is not None:
            self._finished.set()

    def register(self) -> "virEventAsyncIOImpl":
        '''Register this instance as event loop implementation'''
        # pylint: disable=bad-whitespace
        self.log.debug('register()')
        libvirt.virEventRegisterImpl(
            self._add_handle, self._update_handle, self._remove_handle,
            self._add_timeout, self._update_timeout, self._remove_timeout)
        return self

    def schedule_ff_callback(self, iden: int, opaque: _T) -> None:
        '''Schedule a ff callback from one of the handles or timers'''
        asyncio.ensure_future(self._ff_callback(iden, opaque), loop=self.loop)

    async def _ff_callback(self, iden: int, opaque: _T) -> None:
        '''Directly free the opaque object

        This is a coroutine.
        '''
        self.log.debug('ff_callback(iden=%d, opaque=...)', iden)
        libvirt.virEventInvokeFreeCallback(opaque)
        self._pending_dec()

    async def drain(self) -> None:
        '''Wait for the implementation to become idle.

        This is a coroutine.
        '''
        self.log.debug('drain()')
        if self._pending:
            assert self._finished is None
            self._finished = asyncio.Event()
            await self._finished.wait()
            self._finished = None
            assert self._pending == 0
        self.log.debug('drain ended')

    def is_idle(self) -> bool:
        '''Returns False if there are leftovers from a connection

        Those may happen if there are sematical problems while closing
        a connection. For example, not deregistered events before .close().
        '''
        return not self.callbacks and not self._pending

    def _add_handle(self, fd: int, event: int, cb: libvirt._EventCB, opaque: _T) -> int:
        '''Register a callback for monitoring file handle events

        :param int fd: file descriptor to listen on
        :param int event: bitset of events on which to fire the callback
        :param cb: the callback to be called when an event occurrs
        :param opaque: user data to pass to the callback
        :rtype: int
        :returns: handle watch number to be used for updating and unregistering for events

        .. seealso::
            https://libvirt.org/html/libvirt-libvirt-event.html#virEventAddHandleFuncFunc
        '''
        callback = FDCallback(self, cb, opaque,
                              descriptor=self.descriptors[fd], event=event)
        assert callback.iden not in self.callbacks

        self.log.debug('add_handle(fd=%d, event=%d, cb=..., opaque=...) = %d',
                       fd, event, callback.iden)
        self.callbacks[callback.iden] = callback
        self.descriptors[fd].add_handle(callback)
        self._pending_inc()
        return callback.iden

    def _update_handle(self, watch: int, event: int) -> None:
        '''Change event set for a monitored file handle

        :param int watch: file descriptor watch to modify
        :param int event: new events to listen on

        .. seealso::
            https://libvirt.org/html/libvirt-libvirt-event.html#virEventUpdateHandleFunc
        '''
        self.log.debug('update_handle(watch=%d, event=%d)', watch, event)
        callback = self.callbacks[watch]
        assert isinstance(callback, FDCallback)
        callback.update(event=event)

    def _remove_handle(self, watch: int) -> int:
        '''Unregister a callback from a file handle.

        :param int watch: file descriptor watch to stop listening on
        :returns: -1 on error, 0 on success

        .. seealso::
            https://libvirt.org/html/libvirt-libvirt-event.html#virEventRemoveHandleFunc
        '''
        self.log.debug('remove_handle(watch=%d)', watch)
        try:
            callback = self.callbacks.pop(watch)
        except KeyError as err:
            self.log.warning('remove_handle(): no such handle: %r', err.args[0])
            return -1
        assert isinstance(callback, FDCallback)
        fd = callback.descriptor.fd
        assert callback is self.descriptors[fd].remove_handle(watch)
        if len(self.descriptors[fd].callbacks) == 0:
            del self.descriptors[fd]
        callback.close()
        return 0

    def _add_timeout(self, timeout: int, cb: libvirt._TimerCB, opaque: _T) -> int:
        '''Register a callback for a timer event

        :param int timeout: the timeout to monitor
        :param cb: the callback to call when timeout has expired
        :param opaque: user data to pass to the callback
        :rtype: int
        :returns: a timer value

        .. seealso::
            https://libvirt.org/html/libvirt-libvirt-event.html#virEventAddTimeoutFunc
        '''
        callback = TimeoutCallback(self, cb, opaque)
        assert callback.iden not in self.callbacks

        self.log.debug('add_timeout(timeout=%d, cb=..., opaque=...) = %d',
                       timeout, callback.iden)
        self.callbacks[callback.iden] = callback
        callback.update(timeout=timeout)
        self._pending_inc()
        return callback.iden

    def _update_timeout(self, timer: int, timeout: int) -> None:
        '''Change frequency for a timer

        :param int timer: the timer to modify
        :param int timeout: the new timeout value in ms

        .. seealso::
            https://libvirt.org/html/libvirt-libvirt-event.html#virEventUpdateTimeoutFunc
        '''
        self.log.debug('update_timeout(timer=%d, timeout=%d)', timer, timeout)
        callback = self.callbacks[timer]
        assert isinstance(callback, TimeoutCallback)
        callback.update(timeout=timeout)

    def _remove_timeout(self, timer: int) -> int:
        '''Unregister a callback for a timer

        :param int timer: the timer to remove
        :returns: -1 on error, 0 on success

        .. seealso::
            https://libvirt.org/html/libvirt-libvirt-event.html#virEventRemoveTimeoutFunc
        '''
        self.log.debug('remove_timeout(timer=%d)', timer)
        try:
            callback = self.callbacks.pop(timer)
        except KeyError as err:
            self.log.warning('remove_timeout(): no such timeout: %r', err.args[0])
            return -1
        callback.close()
        return 0


_current_impl = None  # type: Optional[virEventAsyncIOImpl]


def getCurrentImpl() -> Optional[virEventAsyncIOImpl]:
    '''Return the current implementation, or None if not yet registered'''
    return _current_impl


def virEventRegisterAsyncIOImpl(loop: asyncio.AbstractEventLoop = None) -> virEventAsyncIOImpl:
    '''Arrange for libvirt's callbacks to be dispatched via asyncio event loop

    The implementation object is returned, but in normal usage it can safely be
    discarded.
    '''
    global _current_impl
    _current_impl = virEventAsyncIOImpl(loop=loop).register()
    return _current_impl
