import os, sys

current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.normpath(os.path.join(current_path, './')))
sys.path.append(os.path.normpath(os.path.join(current_path, '../')))

import morai_actor_pb2
import morai_type_pb2
import morai_simulation_pb2
import moraikit.types

def ToLocationMsg(msg, vector):
    msg.x = vector.x
    msg.y = vector.y
    msg.z = vector.z


def ToRotationMsg(msg, rotation):
    msg.x = rotation.roll
    msg.y = rotation.pitch
    msg.z = rotation.yaw


def from_vector3_msg(msg):
    return moraikit.types.Vector3(msg.x, msg.y, msg.z)


def to_vector3_msg(msg, vector):
    msg.x = vector.x
    msg.y = vector.y
    msg.z = vector.z

def from_location_msg(msg):
    return moraikit.types.Location(msg.x, msg.y, msg.z)


def from_rotation_msg(msg):
    return moraikit.types.Rotation(msg.x, msg.y, msg.z)


def from_actor_state_msg(msg):
    actor_state = moraikit.types.ActorState()
    if msg != None:
        actor_state.actor_info.role_name = msg.actor_info.actor_id
        actor_state.actor_info.actor_type = msg.actor_info.actor_type
        actor_state.bounding_box = from_bounding_box_msg(msg.bounding_box)
        from_transform_msg(actor_state.transform, msg.transform)
        actor_state.velocity = from_vector3_msg(msg.velocity)
        actor_state.angular_velocity = from_vector3_msg(msg.angular_velocity)
        actor_state.acceleration = from_vector3_msg(msg.acceleration)
        actor_state.vehicle_state = from_vehicle_state_msg(msg.vehicle_state)

    return actor_state


def from_network_item_msg(msg):
    network_item = moraikit.types.NetworkItem()
    network_item.network_item_type = msg.type
    network_item.value = msg.value

    return network_item


def from_network_protocol_setting_msg(msg):
    protocol_setting = moraikit.types.NetworkProtocolSetting()
    if msg != None:
        protocol_setting.comm_type = msg.comm_type
        for setting in msg.items:
            protocol_item = moraikit.types.NetworkProtocolItem()
            protocol_item.pubsub_type = setting.protocol
            for item in setting.items:
                protocol_item.network_items.append(from_network_item_msg(item))
            protocol_setting.protocol_items.append(protocol_item)

    return protocol_setting


def from_bounding_box_msg(msg):
    bounding_box = moraikit.types.BoundingBox()
    bounding_box.extent = from_vector3_msg(msg.extent)
    bounding_box.location = from_vector3_msg(msg.location)
    bounding_box.rotation = from_vector3_msg(msg.rotation)

    return bounding_box


def from_vehicle_state_msg(msg):
    vehicle_state = moraikit.types.VehicleState()
    vehicle_state.throttle = msg.throttle
    vehicle_state.steer = msg.steer
    vehicle_state.brake = msg.brake
    vehicle_state.front_wheel_angle = msg.front_wheel_angle
    vehicle_state.gear_mode = msg.gear_mode
    vehicle_state.vehicle_aux_state = from_vehicle_aux_state_msg(msg.aux_state)

    return vehicle_state


def from_vehicle_aux_state_msg(msg):
    vehicle_aux_state = moraikit.types.VehicleAuxState()
    vehicle_aux_state.current_link_info = from_link_info_msg(msg.current_link_info)
    vehicle_aux_state.remaining_distance = msg.remaining_distance
    vehicle_aux_state.is_pass_dest_pos = msg.is_pass_des_pos
    vehicle_aux_state.tl_id = msg.tl_id
    vehicle_aux_state.tl_color = msg.tl_color
    vehicle_aux_state.is_collision = msg.is_collision

    return vehicle_aux_state


def from_link_info_msg(msg):
    link_info = moraikit.types.LinkInfo()
    link_info.unique_id = msg.unique_id
    link_info.waypoint_idx = msg.waypoint_idx

    return link_info


def to_link_info_msg(link_info):
    msg = morai_type_pb2.LinkInfo()
    msg.unique_id = link_info.unique_id
    msg.waypoint_idx = link_info.waypoint_idx

    return msg


def from_tl_info_msg(msg):
    tl_info = moraikit.types.TrafficLightInfo()
    if msg is not None :
        tl_info.success = msg.success
        tl_info.tl_id = msg.tl_id
        tl_info.tl_color = msg.tl_color

    return tl_info


def to_transform_msg(msg, transform):
    ToLocationMsg(msg.location, transform.location)
    ToRotationMsg(msg.rotation, transform.rotation)


def from_transform_msg(transform, msg):
    transform.location = from_location_msg(msg.location)
    transform.rotation = from_rotation_msg(msg.rotation)


def to_raycast_param_msg(source, target, max_dist):
    msg = morai_simulation_pb2.RaycastParam()
    ToLocationMsg(msg.source, source)
    ToLocationMsg(msg.target, target)
    msg.max_dist = max_dist

    return msg


def to_vehicle_ctrl_cmd_msg(role_name, vehicle_control):
    msg = morai_actor_pb2.VehicleCtrlCmd()
    msg.actor_id = role_name
    msg.long_cmd_type = 1
    msg.throttle = vehicle_control.throttle
    msg.steer = vehicle_control.steer
    msg.brake = vehicle_control.brake
    msg.velocity = 0
    msg.acceleration = 0

    return msg    


def to_actor_info_msg(actor_info):
    msg = morai_actor_pb2.ActorInfo()
    msg.actor_id = actor_info.role_name
    msg.actor_type = actor_info.actor_type

    return msg


def to_network_item_msg(network_item):
    msg = morai_actor_pb2.NetworkItem()
    msg.type = network_item.network_item_type
    msg.value = network_item.value

    return msg


def to_network_ip_setting_msg(ip_item):
    msg = morai_actor_pb2.NetworkIpSetting()
    msg.connect_type = ip_item.connect_type

    for item in ip_item.network_items:
        msg.items.append(to_network_item_msg(item))

    return msg


def to_network_protocol_item_msg(protocol_item):
    msg = morai_actor_pb2.NetworkProtocolItem()
    msg.protocol = protocol_item.pubsub_type

    for item in protocol_item.network_items:
        msg.items.append(to_network_item_msg(item))

    return msg


# def to_network_protocol_setting_msg(protocol_setting):
#     msg = morai_actor_pb2.NetworkProtocolSetting()
#     msg.comm_type = protocol_setting.comm_type
#     for protocol_item in protocol_setting.protocol_items:
#         msg.items.append(to_network_protocol_item_msg(protocol_item))

#     return msg


def to_network_config_msg(msg, setting):
    msg.enabled = setting.enabled    
    msg.actor_info.actor_id = setting.actor_info.role_name
    msg.actor_info.actor_type = setting.actor_info.actor_type
    msg.comm_type = setting.comm_type
    msg.frame_rate = setting.frame_rate

    for ip_item in setting.ip_settings:        
        msg.ip_settings.append(to_network_ip_setting_msg(ip_item))

    msg.protocol_settings.comm_type = setting.comm_type
    for protocol_item in setting.protocol_settings.protocol_items:
        msg.protocol_settings.items.append(to_network_protocol_item_msg(protocol_item))

def to_vehicle_event_control_msg(msg, vehicle_event_control):
    msg.option = vehicle_event_control.option
    msg.ctrl_mode = vehicle_event_control.ctrl_mode
    msg.gear = vehicle_event_control.gear
    msg.turn_signal = vehicle_event_control.turn_signal
    msg.emergency_signal = vehicle_event_control.emergency_signal
    msg.set_pause = vehicle_event_control.set_pause

def to_actor_property_msg(actor_property):
    msg = morai_actor_pb2.ActorProperty()
    msg.actor_info.actor_id = actor_property.actor_info.role_name
    msg.actor_info.actor_type = actor_property.actor_info.actor_type
    msg.type = actor_property.type
    if msg.type == moraikit.types.ActorPropertyType.ACTOR_PROPERTY_TRANSFORM:
        to_transform_msg(msg.transform, actor_property.transform)
    elif msg.type == moraikit.types.ActorPropertyType.ACTOR_PROPERTY_NETWORK:
        to_network_config_msg(msg.network, actor_property.network)
    elif msg.type == moraikit.types.ActorPropertyType.ACTOR_PROPERTY_PHYSICS:
        msg.physics = actor_property.physics
    elif msg.type == moraikit.types.ActorPropertyType.ACTOR_PROPERTY_AI:
        msg.ai = actor_property.ai
    elif msg.type == moraikit.types.ActorPropertyType.ACTOR_PROPERTY_VEHICLE_EVENT:
        to_vehicle_event_control_msg(msg.vehicle_event_control, actor_property.vehicle_event_control)

    return msg


def to_ego_ctrl_cmd(ego_ctrl_cmd):
    msg = morai_actor_pb2.EgoCtrlCmd()
    to_transform_msg(msg.transform, ego_ctrl_cmd.transform)
    msg.velocity = ego_ctrl_cmd.velocity
    msg.pause = ego_ctrl_cmd.pause
    to_ego_cruise_ctrl_msg(msg.cruise_settings, ego_ctrl_cmd.cruise_settings)

    return msg


def to_ego_cruise_ctrl_msg(msg, ego_cruise_ctrl):
    msg.cruise_on = ego_cruise_ctrl.cruise_on
    msg.cruise_type = ego_cruise_ctrl.cruise_type
    msg.link_speed_ratio = ego_cruise_ctrl.link_speed_ratio
    msg.constant_velocity = ego_cruise_ctrl.constant_velocity

    return msg


def to_vehicle_route_msg(vehicle_route):
    msg = morai_actor_pb2.VehicleRoute()
    msg.actor_info.actor_id = vehicle_route.actor_info.role_name
    msg.actor_info.actor_type = vehicle_route.actor_info.actor_type
    msg.vehicle_type = vehicle_route.vehicle_type
    msg.decision_range = vehicle_route.decision_range
    for link in vehicle_route.link_list:
        msg.links.append(to_link_info_msg(link))

    return msg

def to_vehicle_destination_msg(vehicle_destination):
    msg = morai_actor_pb2.VehicleDestination()
    msg.actor_info.actor_id = vehicle_destination.actor_info.role_name
    msg.actor_info.actor_type = vehicle_destination.actor_info.actor_type
    msg.vehicle_type = vehicle_destination.vehicle_type
    msg.decision_range = vehicle_destination.decision_range
    to_vector3_msg(msg.position, vehicle_destination.position)

    return msg
