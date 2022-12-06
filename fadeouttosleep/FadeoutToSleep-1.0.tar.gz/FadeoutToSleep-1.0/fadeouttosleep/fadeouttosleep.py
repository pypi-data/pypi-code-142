#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This project uses code that is MIT licensed: pulsectl https://github.com/mk-fg/python-pulse-control

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, Pango
from pathlib import Path
import sys
import os
import time

from pulsectl import pulsectl, PulseVolumeInfo

class FadeoutToSleepWindow(Gtk.Window):
    def __init__(self):
        self.startvolume = None
        self.channelcount = None
        self.startmute = 0
        self.minutes = 30
        self.hours = 0
        self.fadeout = True
        self.standby = True
        self.minutestostart = 0
        self.minutesbeforeend = 0

        self.isrunning = False
        self.isdone = False
        self.starttime = 0.0
        self.endtime = 0.0
        self.totalrunseconds = 0
        
        self.controller = None
        self.maxvolume = None
        self.device = None
        self.defaultsink = None
        self.pulse = pulsectl.Pulse('FadeoutToSleep')

        try:
            with open(str(Path.home()) + '/.FadeoutToSleep/config', 'r') as file:
                for line in file:
                    parts = line.split('=')
                    if parts[0] == 'Device':
                        #print("found device:" + parts[1].strip())
                        try:
                            self.device = int(parts[1])
                        except:
                            print("error on device")
                            pass

                    if parts[0] == 'Minutes':
                        #print("found minutes::" + parts[1].strip())
                        try:
                            self.minutes = int(parts[1])
                        except:
                            print("error on minutes")
                            pass
                    if parts[0] == 'Hours':
                        #print("found hours:" + parts[1].strip())
                        try:
                            self.hours = int(parts[1])
                        except:
                            print("error on hours")
                            pass
                    if parts[0] == 'Fadeout':
                        #print("found fadeout: " + parts[1].strip() + " Line: " + line)
                        if parts[1][0:4] == "True":
                            self.fadeout = True
                        else:
                            self.fadeout = False

                    if parts[0] == 'Standby':
                        #print("found standby: " + parts[1].strip() + " Line: " + line)
                        if parts[1][0:4] == "True":
                            self.standby = True
                        else:
                            self.standby = False

                    if parts[0] == 'FadeoutStart':
                        #print("found fadeout start: " + parts[1].strip())
                        self.minutestostart = int(parts[1])

                    if parts[0] == 'FadeoutEnd':
                        #print("found fadeout end: " + parts[1].strip())
                        self.minutesbeforeend = int(parts[1])
                    

        except FileNotFoundError:
            print("No config file.")
        except:
            print("Error during file reading:", sys.exc_info()[0])
            pass

        self.screen = Gdk.Screen.get_default()
        self.provider = Gtk.CssProvider()
        self.stylecontext = Gtk.StyleContext()
        self.stylecontext.add_provider_for_screen(self.screen, self.provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        #provider.load_from_path("FadeoutToSleep.css")
        #Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        scriptdir = os.path.dirname(__file__)
        self.gladefile = os.path.join(scriptdir, "Glade/FadeoutToSleep.glade")

        #self.gladefile = "SilentSleep.glade"

        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("mainwindow")

        self.window.connect("destroy", Gtk.main_quit) ## this was the one that actually worked!
        self.deviceboxcontents = self.builder.get_object("liststore2")
        self.ourprogressbar = self.builder.get_object("timeprogress")
        self.ourdevice = self.builder.get_object("combobox2")
        self.ourdevicelabel = self.builder.get_object("device_info")
        ourcellrenderer = self.builder.get_object("devicecellrenderer")
        self.ouraboutwindow = self.builder.get_object("aboutdialog1")
        self.ouraiwindow = self.builder.get_object("additional_info_dialog")

        self.ourstartbutton = self.builder.get_object("start_button")
        self.ourimage = self.builder.get_object("state_image")
        self.ourstate = self.builder.get_object("state_text")
        self.ourminutes = self.builder.get_object("minutes_selection")
        self.ourhours = self.builder.get_object("hours_selection")
        self.ourstandby = self.builder.get_object("standby_switch")
        self.ourfadeout = self.builder.get_object("fade_out_switch")
        self.ourfadeoutstart = self.builder.get_object("fadeout_start_selection")
        self.ourfadeoutend = self.builder.get_object("fadeout_end_selection")
        self.ourcounter = self.builder.get_object("counter_label")
        self.erroricon = self.builder.get_object("device_error_image")
        
        css = b"""
        #progressbox {
          min-height: 28px;
        }
        
        .oma progress, trough {
          background: none;
          background-color: transparent;
          min-height: 28px;
        }

        .oma progress, full {
          background-color: green;
        }

        """
        self.provider.load_from_data(css)
        
        self.ourprogressbar.set_fraction(0.0)        

        if not self.minutes == None:
            self.ourminutes.set_value(self.minutes)

        if not self.hours == None:
            self.ourhours.set_value(self.hours)

        if self.standby == True:
            self.ourstandby.set_state(True)
        else:
            self.ourstandby.set_state(False)

        if self.fadeout == True:
            self.ourfadeout.set_state(True)
        else:
            self.ourfadeout.set_state(False)

        if not self.minutestostart == None:
            self.ourfadeoutstart.set_value(int(self.minutestostart))

        if not self.minutesbeforeend == None:
            self.ourfadeoutend.set_value(int(self.minutesbeforeend))

        self.window.show()

        #print(self.pulse.server_info().default_sink_name)      

        #self.deviceboxcontents.clear()
        for iter, i in enumerate(self.pulse.sink_list()):
            deviceentry = (i.name, i.description, i.index, iter)
            #print(deviceentry)
            self.deviceboxcontents.append(deviceentry)

        ourcellrenderer.set_property("ellipsize", Pango.EllipsizeMode.END)
        ourcellrenderer.set_fixed_size(20, -1)

        if not self.device == None and self.device < len(self.deviceboxcontents):
            #print("Device valid")
            self.ourdevice.set_active(self.device) # make this resolve the real value from index
            ourlabel = ("ID" + str(self.deviceboxcontents[self.device][2]) + ": " + self.deviceboxcontents[self.device][0] + 
                        " / " + self.deviceboxcontents[self.device][1])
            self.ourdevicelabel.set_text(ourlabel)
            self.channelcount = len(self.pulse.sink_list()[self.deviceboxcontents[self.device][3]].volume.values)
            self.startvolume = PulseVolumeInfo(0.5, self.channelcount)
            #self.startvolume = self.pulse.sink_list()[self.deviceboxcontents[self.device][3]].volume.value_flat
        else:
            self.erroricon.set_visible(True)        
        
    def do_update(self):
        if self.isrunning:
            totalsecondsleft = int((self.endtime + 1) - time.time())
            hoursleft = int((totalsecondsleft / 60) / 60)
            minutesleft = int(totalsecondsleft / 60) - (hoursleft * 60)
            secondsleft = totalsecondsleft - (hoursleft * 60 * 60) - (minutesleft * 60)
                    
            self.ourprogressbar.set_fraction(totalsecondsleft / self.totalrunseconds)
            #print(totalsecondsleft, " / ", totalsecondsleft / self.totalrunseconds)

            if totalsecondsleft / self.totalrunseconds <= 0.10:
                css = b"""
                #progressbox {
                  min-height: 28px;
                }
                
                .oma progress, trough {
                  background: none;
                  background-color: transparent;
                  min-height: 28px;
                }

                .oma progress, full {
                  background-color: red;
                }

                """
                self.provider.load_from_data(css)
            elif totalsecondsleft / self.totalrunseconds <= 0.33:
                css = b"""
                #progressbox {
                  min-height: 28px;
                }
                
                .oma progress, trough {
                  background: none;
                  background-color: transparent;
                  min-height: 28px;
                }

                .oma progress, full {
                  background-color: yellow;
                }

                """
                self.provider.load_from_data(css)
            
            self.ourcounter.set_text(str(hoursleft).zfill(2) + ":" + str(minutesleft).zfill(2) + ":" + str(secondsleft).zfill(2))
            
            tempvolume = PulseVolumeInfo(0.5, self.channelcount)
            for iter, volumevalue in enumerate(self.startvolume.values):
                tempvolume.values[iter] = ((volumevalue / self.maxvolume) * ((totalsecondsleft - self.minutesbeforeend * 60) / 
                                            (self.totalrunseconds - self.minutestostart * 60 - self.minutesbeforeend * 60)))
                #print("iter:", iter, " volumevalue:", volumevalue)

            if (not self.fadeout) or self.device == None or (time.time() < (self.starttime + self.minutestostart * 60)):
                #print("do nothing yet or no fadeout")    
                return   
            elif totalsecondsleft > (self.minutesbeforeend * 60):
                #print((self.startvolume.value_flat / self.maxvolume), " - ", tempvolume)
                
                tempsink = self.pulse.sink_list()[self.deviceboxcontents[self.device][3]]
                self.pulse.volume_set(tempsink, tempvolume)

            else:
                if self.fadeout and tempvolume.value_flat >= 0.0:
                    #print("Last volume lowering: ", tempvolume)
                    tempsink = self.pulse.sink_list()[self.deviceboxcontents[self.device][3]]
                    self.pulse.volume_set(tempsink, tempvolume)
                #print("stop doing things")

            if totalsecondsleft <= 0:
                self.ourstartbutton.set_label("Reset")
                self.ourimage.set_from_icon_name('gtk-apply', Gtk.IconSize.LARGE_TOOLBAR)
                self.ourstate.set_text("Done")
                self.ourminutes.set_editable(True)
                self.ourhours.set_editable(True)
                # And in case the program was left running when sleep was manually activated or something:
                if totalsecondsleft >= -60:
                    self.isdone = True
                    self.isrunning = False
                    self.ourcounter.set_text(str(hoursleft).zfill(2) + ":" + str(minutesleft).zfill(2) + ":" + 
                                        str(secondsleft).zfill(2))
                    if self.standby:
                        #GO TO SLEEP
                        #print("Computer going to sleep")
                        os.system("systemctl suspend")
                    return True
                else:
                    self.isrunning = False
                    print("Computer went to sleep or or total halt while the program was running.")
                    return False
            
            return True
        else:
            return False

    def on_gtk_quit_activate(self, menuitem, data=None):
        Gtk.main_quit()

    def on_mainwindow_destroy(self, object, data=None):
        Gtk.main_quit()

    def close_button_clicked(self, button):
        # maybe set to startvolume here in case the program was running
        self.pulse.close()
        #self.controller.close()
        Gtk.main_quit()

    def about_button_clicked(self, button):
        self.ouraboutwindow.run()
        self.ouraboutwindow.hide()

    def additional_info_clicked(self, button):
        ouraibutton = self.builder.get_object("additional_info_close_button")
        mainwindowpos = self.window.get_position()
        mainwindowsize = self.window.get_size()
        aiwindowpos = self.ouraiwindow.get_position()
        aiwindowsize = self.ouraiwindow.get_size()

        # Window style properties:
        # "decoration-button-layout 	
        # "decoration-resize-handle
        # "resize-grip-height
        # "resize-grip-width
        # Dialog window style properties:
        # "action-area-border"
        # "button-spacing"
        # "content-area-border"      
        # "content-area-spacing" 

        #print(self.window.list_style_properties()) # List all properties, useful!
          
        padding = self.window.style_get_property('focus-padding')
        aipadding = self.ouraiwindow.style_get_property('focus-padding')
        airesizehandle = self.ouraiwindow.style_get_property('decoration-resize-handle')
        actionborder = self.ouraiwindow.style_get_property('action-area-border')
        contentborder = self.ouraiwindow.style_get_property('content-area-border')
        
        # I have no idea if the paddings etc are calculated correctly, cause there NO documentation.
        self.ouraiwindow.move(mainwindowpos[0] + mainwindowsize[0] + padding + aipadding, 
                              mainwindowpos[1] + airesizehandle + actionborder + (contentborder * 2))
        
        self.ouraiwindow.connect('delete_event', self.closetohide) # make close button hide the window
        self.ouraiwindow.show()
        self.ouraiwindow.activate()
        self.ouraiwindow.grab_focus()

        ouraibutton.grab_focus()
        self.ouraiwindow.set_focus_child(ouraibutton)

    def closetohide(self, event, userdata):
        self.ouraiwindow.hide()
        return True # Do not go further
        
    def additional_info_close_clicked(self, button):
        self.ouraiwindow.hide()

    def minutes_changed(self, button):
        self.minutes = int(self.ourminutes.get_value())
        if not self.hours == None:
            if not self.minutes == None:
                self.ourcounter.set_text(str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) + ":00")
        self.write_config()

    def hours_changed(self, button):
        self.hours = int(self.ourhours.get_value())
        if not self.hours == None:
            if not self.minutes == None:
                self.ourcounter.set_text(str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) + ":00")
        self.write_config()


    def device_changed(self, button):
        #print ("Device changed: ", self.ourdevice.get_model()[self.ourdevice.get_active()][0], 
        #       "iter: ",self.ourdevice.get_model()[self.ourdevice.get_active()][3], 
        #       "ID: ", self.ourdevice.get_model()[self.ourdevice.get_active()][2])
        self.device = self.ourdevice.get_model()[self.ourdevice.get_active()][3]
        ourlabel = ("ID" + str(self.deviceboxcontents[self.device][2]) + ": " + 
                    self.deviceboxcontents[self.device][0] + " / " + self.deviceboxcontents[self.device][1])
        self.ourdevicelabel.set_text(ourlabel)
        self.write_config()
        self.erroricon.set_visible(False)

    def fadeout_state_changed(self, switch, state):
        self.fadeout = state
        self.write_config()
        return

    def standby_state_changed(self, switch, state):
        self.standby = state
        self.write_config()
        return

    def fade_start_changed(self, button):
        self.minutestostart = int(button.get_value())
        self.write_config()

    def fade_end_changed(self, button):
        self.minutesbeforeend = int(button.get_value())
        self.write_config()

    def start_button_clicked(self, button):
        if not self.device == None and self.device < len(self.deviceboxcontents):
            self.startmute = self.pulse.sink_list()[self.deviceboxcontents[self.device][3]].mute
            #print("Startmute: ", self.startmute)
        else:
            print("Device not valid")
            return False;

        totalminutes = (self.hours * 60) + self.minutes

        if ((not self.isdone) and (not self.isrunning) and (self.hours + self.minutes > 0) and 
            (totalminutes > self.minutestostart + self.minutesbeforeend) and self.startmute == 0):
            self.ourprogressbar.set_fraction(1.0)
            self.ourfadeout.set_property("sensitive", False)
            self.ourdevice.set_property("sensitive", False)

            self.channelcount = len(self.pulse.sink_list()[self.deviceboxcontents[self.device][3]].volume.values)
            self.startvolume = self.pulse.sink_list()[self.deviceboxcontents[self.device][3]].volume

            self.maxvolume = 1.0
            #print("Startvolume", self.startvolume)
            #self.maxvolume = self.controller.get_vol_max_norm()
            self.isrunning = True
            #self.isdone = False
            GLib.timeout_add(200, self.do_update) # Update program every 200ms
            if self.isdone:
                self.ourstartbutton.set_label("Reset")
            else:
                self.ourstartbutton.set_label("Stop")
            self.ourimage.set_from_icon_name('gtk-media-play', Gtk.IconSize.LARGE_TOOLBAR)
            self.starttime = time.time()
            self.endtime = self.starttime + (self.hours * 60 * 60) + (self.minutes * 60)
            self.totalrunseconds = self.endtime - self.starttime
            #print("Total: ", self.totalrunseconds, " Time: ", self.starttime)
            self.ourstate.set_text("Running")
            self.ourminutes.set_property("sensitive", False)
            self.ourhours.set_property("sensitive", False)
            self.ourfadeoutstart.set_property("sensitive", False)
            self.ourfadeoutend.set_property("sensitive", False)
        else:
            self.ourfadeout.set_property("sensitive", True)            
            self.ourdevice.set_property("sensitive", True)
            self.isrunning = False
            self.ourstartbutton.set_label("Sleepysleep")
            self.ourimage.set_from_icon_name('gtk-media-stop', Gtk.IconSize.LARGE_TOOLBAR)
            self.ourstate.set_text("Stopped")
            self.ourminutes.set_property("sensitive", True)
            self.ourhours.set_property("sensitive", True)
            self.ourfadeoutstart.set_property("sensitive", True)
            self.ourfadeoutend.set_property("sensitive", True)
            self.ourprogressbar.set_fraction(1.0)
            
            if self.fadeout and (not self.device == None):
                tempsink = self.pulse.sink_list()[self.deviceboxcontents[self.device][3]]
                self.pulse.volume_set(tempsink, self.startvolume)
                #print("Volume set back to: ", self.startvolume.value_flat)

            if not self.hours == None:
                if not self.minutes == None:
                    self.ourcounter.set_text(str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) + ":00")

            css = b"""
            #progressbox {
              min-height: 28px;
            }
            
            .oma progress, trough {
              background: none;
              background-color: transparent;
              min-height: 28px;
            }

            .oma progress, full {
              background-color: green;
            }

            """
            self.provider.load_from_data(css)

            self.isdone = False

    def write_config(self):
        if not os.path.isdir(str(Path.home()) + '/.FadeoutToSleep'):
            os.mkdir(str(Path.home()) + '/.FadeoutToSleep')
            print ("Made a config directory")
        try:
            with open(str(Path.home()) + '/.FadeoutToSleep/config', 'w') as file:
                line = ("Device=" + str(self.device) + "\n")
                file.write(line)
                line = ("Minutes=" + str(self.minutes) + "\n")
                file.write(line)
                line = ("Hours=" + str(self.hours) + "\n")
                file.write(line)
                line = ("Standby=" + str(self.standby) + "\n")
                file.write(line)
                line = ("Fadeout=" + str(self.fadeout) + "\n")
                file.write(line)
                line = ("FadeoutStart=" + str(self.minutestostart) + "\n")
                file.write(line)
                line = ("FadeoutEnd=" + str(self.minutesbeforeend) + "\n")
                file.write(line)
                #print("Wrote config file")
        except:
            print("Can't write config file")   

def mymain():
    main = FadeoutToSleepWindow()
    Gtk.main()

if __name__ == "__main__":
    mymain()

