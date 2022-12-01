import numpy as np
from common_utils.transformation import get_tr, r2rpy, iso2unity, unity2iso
from enum import IntEnum

class GearMode(IntEnum):
    GEAR_MODE_M = 0
    GEAR_MODE_P = 1
    GEAR_MODE_R = 2
    GEAR_MODE_N = 3
    GEAR_MODE_D = 4
    GEAR_MODE_L = 5

class ActorType(IntEnum):    
    ACTOR_TYPE_UNKNOWN = 0
    ACTOR_TYPE_VEHICLE = 1
    ACTOR_TYPE_PEDESTRIAN = 2
    ACTOR_TYPE_OBSTACLE = 3

class ActorPropertyType(IntEnum):
    ACTOR_PROPERTY_TRANSFORM = 0
    ACTOR_PROPERTY_NETWORK = 1
    ACTOR_PROPERTY_PHYSICS = 2
    ACTOR_PROPERTY_AI = 3
    ACTOR_PROPERTY_VEHICLE_EVENT = 4

class NetworkCommType(IntEnum):
    NETWORK_COMM_TYPE_BEGIN = 0
    NETWORK_COMM_TYPE_UDP = 1
    NETWORK_COMM_TYPE_TCP = 2
    NETWORK_COMM_TYPE_ROS = 3
    NETWORK_COMM_TYPE_LCM = 4
    NETWORK_COMM_TYPE_SERIAL = 5
    NETWORK_COMM_TYPE_ROS_AUTO = 6
    NETWORK_COMM_TYPE_APOLLO = 7
    NETWORK_COMM_TYPE_END = 8

class NetworkItemType(IntEnum):
    NETWORK_ITEM_TYPE_BEGIN = 0
    NETWORK_ITEM_TYPE_HOST_IP = 1
    NETWORK_ITEM_TYPE_DESTINATION_IP = 2
    NETWORK_ITEM_TYPE_BRIDGE_IP = 3
    NETWORK_ITEM_TYPE_HOST_PORT = 4
    NETWORK_ITEM_TYPE_DESTINATION_PORT = 5
    NETWORK_ITEM_TYPE_BRIDGE_PORT = 6
    NETWORK_ITEM_TYPE_MESSAGE_TYPE = 7
    NETWORK_ITEM_TYPE_MESSAGE_TOPIC = 8
    NETWORK_ITEM_TYPE_MESSAGE_CHANNEL = 9
    NETWORK_ITEM_TYPE_SERIAL_FIELD = 10
    NETWORK_ITEM_TYPE_SERIAL_PORTNUMBER = 11
    NETWORK_ITEM_TYPE_SERIAL_BAUDRATE = 12
    NETWORK_ITEM_TYPE_SERIAL_PARITY = 13
    NETWORK_ITEM_TYPE_SERIAL_DATABITS = 14
    NETWORK_ITEM_TYPE_SERIAL_STOPBITS = 15
    NETWORK_ITEM_TYPE_SERIAL_FLOWCONTROL = 16
    NETWORK_ITEM_TYPE_SERVCIE_NAME = 17
    NETWORK_ITEM_TYPE_SRV = 18
    NETWORK_ITEM_TYPE_FRAME_ID = 19
    NETWORK_ITEM_TYPE_CHILDFRAME_ID = 20
    NETWORK_ITEM_TYPE_END = 21

class PUBSUBType(IntEnum):
    PUBSUB_TYPE_BEGIN = 0
    PUBSUB_TYPE_Common = 256
    PUBSUB_TYPE_ObjectInfoPublisher = 257
    PUBSUB_TYPE_TLStatusPublisher = 258
    PUBSUB_TYPE_TLCtrlSubscriber = 259
    PUBSUB_TYPE_MultiEgoTransformHandler = 260
    PUBSUB_TYPE_CollisionData = 261
    PUBSUB_TYPE_SensorPosSubscriber = 262
    PUBSUB_TYPE_GlobalIntersectionPublisher = 263
    PUBSUB_TYPE_IntersectionControlSubscriber = 264
    PUBSUB_TYPE_IntersectionStatusPublisher = 265
    PUBSUB_TYPE_SensorSyncDataSubscriber = 266
    PUBSUB_TYPE_TF2Publisher = 267
    PUBSUB_TYPE_VehicleCollisionInfoPublisher = 268
    PUBSUB_TYPE_SyncModeCmdServiceProvider = 269
    PUBSUB_TYPE_SyncModeWaitForTickServiceProvider = 270
    PUBSUB_TYPE_SyncModeInfoPublisher = 271
    PUBSUB_TYPE_SyncModeAddObjectSubscriber = 272
    PUBSUB_TYPE_SyncModeRemoveObjectSubscriber = 273
    PUBSUB_TYPE_SyncModeSetGearServiceProvider = 274
    PUBSUB_TYPE_SyncModeCtrlCmdServiceProvider = 275
    PUBSUB_TYPE_SyncModeSaveSensorDataServiceProvider = 276
    PUBSUB_TYPE_SyncModeMoraiSLServiceProvider = 277
    PUBSUB_TYPE_MandoObjectInfoPublisher = 278
    PUBSUB_TYPE_HILSMoraiInfoPublisher = 279
    PUBSUB_TYPE_FaultStatusPublisher = 280
    PUBSUB_TYPE_FaultStatusVehicleSubscriber = 281
    PUBSUB_TYPE_AutoeverIFSSubscriber = 282
    PUBSUB_TYPE_FaultStatusWheelSubscriber = 283
    PUBSUB_TYPE_FaultStatusSensorSubscriber = 284
    PUBSUB_TYPE_AutoeverInfoSubscriber = 285
    PUBSUB_TYPE_ERP = 512
    PUBSUB_TYPE_ERPInfoPublisher = 513
    PUBSUB_TYPE_ERPSerialInfoPublisher = 514
    PUBSUB_TYPE_ERPCmdController = 515
    PUBSUB_TYPE_ERPObjectInfoPublisher = 516
    PUBSUB_TYPE_MORAI = 768
    PUBSUB_TYPE_MoraiAutowareInfoPublisher = 769
    PUBSUB_TYPE_MoraiInfoPublisher = 770
    PUBSUB_TYPE_MoraiCmdController = 771
    PUBSUB_TYPE_MoraiObjectInfoPublisher = 772
    PUBSUB_TYPE_MoraiSimProcHandleSubscriber = 773
    PUBSUB_TYPE_MoraiSimProcStatusPublisher = 774
    PUBSUB_TYPE_MoraiSLServiceProvider = 775
    PUBSUB_TYPE_MoraiLampsSubscriber = 776
    PUBSUB_TYPE_MoraiSimProcServiceProvider = 777
    PUBSUB_TYPE_MoraiTLServiceProvider = 778
    PUBSUB_TYPE_MoraiReplayInfoPublisher = 779
    PUBSUB_TYPE_MoraiEventCmdServiceProvider = 780
    PUBSUB_TYPE_MoraiVehicleSpecServiceProvider = 781
    PUBSUB_TYPE_MoraiMapSpecServiceProvider = 782
    PUBSUB_TYPE_MoraiSLSubscriber = 783
    PUBSUB_TYPE_AUTOWARE = 1024
    PUBSUB_TYPE_MoraiAutowareCmdController = 1025
    PUBSUB_TYPE_MoraiAutowareGear = 1026
    PUBSUB_TYPE_NAVER = 1280
    PUBSUB_TYPE_NaverSLSubscriber = 1281
    PUBSUB_TYPE_NaverSimProcHandleSubscriber = 1282
    PUBSUB_TYPE_NaverInfoPublisher_ObdAcceleratorPedal = 1283
    PUBSUB_TYPE_NaverInfoPublisher_ObdGear = 1284
    PUBSUB_TYPE_NaverInfoPublisher_ObdLamps = 1285
    PUBSUB_TYPE_NaverInfoPublisher_ObdSteeringAngle = 1286
    PUBSUB_TYPE_NaverInfoPublisher_ObdWheelSpeeds = 1287
    PUBSUB_TYPE_NaverInfoPublisher_ObdYawRate = 1288
    PUBSUB_TYPE_NaverInfoPublisher_VehiclePose = 1289
    PUBSUB_TYPE_NaverObjectInfoPublisher = 1290
    PUBSUB_TYPE_NaverSimProcStatusPublisher = 1291
    PUBSUB_TYPE_NaverTrafficLightPublisher = 1292
    PUBSUB_TYPE_NaverCmdController = 1293
    PUBSUB_TYPE_NaverSubscriber_ObdLamps = 1294
    PUBSUB_TYPE_NaverSLServiceProvider = 1295
    PUBSUB_TYPE_NaverSimProcServiceProvider = 1296
    PUBSUB_TYPE_NaverTLServiceProvider = 1297
    PUBSUB_TYPE_CBNU = 1536
    PUBSUB_TYPE_CBNUSLSubscriber = 1537
    PUBSUB_TYPE_CBNUCmdController = 1538
    PUBSUB_TYPE_CBNUInfoPublisher = 1539
    PUBSUB_TYPE_CBNUObjectInfoPublisher = 1540
    PUBSUB_TYPE_KAIST = 1792
    PUBSUB_TYPE_KaistSLSubscriber = 1793
    PUBSUB_TYPE_KaistCmdController = 1794
    PUBSUB_TYPE_KaistInfoPublisher = 1795
    PUBSUB_TYPE_KaistObjectInfoPublisher = 1796
    PUBSUB_TYPE_WECAR = 2048
    PUBSUB_TYPE_WeCarCmdController = 2049
    PUBSUB_TYPE_WeCarInfoPublisher = 2050
    PUBSUB_TYPE_WeCarInfoVescStatePublisher = 2051
    PUBSUB_TYPE_WeCarInfoSteerPublisher = 2052
    PUBSUB_TYPE_SSAFY = 2304
    PUBSUB_TYPE_SSAFYCmdController = 2305
    PUBSUB_TYPE_SSAFYTurtleBotInfoPublisher = 2306
    PUBSUB_TYPE_SSAFYObjectStatusPublisher = 2307
    PUBSUB_TYPE_SSAFYObjectControlSubscriber = 2308
    PUBSUB_TYPE_SSAFYEnviromentInfoPublisher = 2309
    PUBSUB_TYPE_SSAFYStuffObjectControlSubscriber = 2310
    PUBSUB_TYPE_SSAFYStuffObjectInfoPublisher = 2311
    PUBSUB_TYPE_KAISTGHOST = 2560
    PUBSUB_TYPE_KaistGhostCmdController = 2561
    PUBSUB_TYPE_MORAIGHOST = 2816
    PUBSUB_TYPE_MoraiGhostCmdController = 2817
    PUBSUB_TYPE_MoraiNpcGhostController = 2818
    PUBSUB_TYPE_SCOUTMINI = 3072
    PUBSUB_TYPE_ScoutCmdController = 3073
    PUBSUB_TYPE_ScoutInfoPublisher = 3074
    PUBSUB_TYPE_ScoutLightCmdSubscriber = 3075
    PUBSUB_TYPE_CYBER = 3328
    PUBSUB_TYPE_CyberCmdController = 3329
    PUBSUB_TYPE_CyberChassisPublisher = 3330
    PUBSUB_TYPE_CyberBestPosePublisher = 3331
    PUBSUB_TYPE_CyberInsStatPublisher = 3332
    PUBSUB_TYPE_CyberOdometryPublisher = 3333
    PUBSUB_TYPE_CyberCorrectedImuPublisher = 3334
    PUBSUB_TYPE_CyberImuPublisher = 3335
    PUBSUB_TYPE_ERPV2 = 3584
    PUBSUB_TYPE_ERPv2CmdController = 3585
    PUBSUB_TYPE_ERPv2InfoPublisher = 3586
    PUBSUB_TYPE_ERPv2ObjectInfoPublisher = 3587
    PUBSUB_TYPE_ERPv2SerialInfoPublisher = 3588
    PUBSUB_TYPE_WEBOT = 3840
    PUBSUB_TYPE_WeBOTCmdController = 3841
    PUBSUB_TYPE_WeBOTInfoSteerPublisher = 3842
    PUBSUB_TYPE_WeBOTInfoVescStatePublisher = 3843
    PUBSUB_TYPE_PR = 4096
    PUBSUB_TYPE_PRCmdController = 4097
    PUBSUB_TYPE_PRStatusPublisher = 4098
    PUBSUB_TYPE_PREventServiceProvider = 4099
    PUBSUB_TYPE_DIFFERETIAL_DRIVE = 4352
    PUBSUB_TYPE_MoraiDdCmdController = 4353
    PUBSUB_TYPE_MoraiDdInfoPublisher = 4354
    PUBSUB_TYPE_END = 4355

class NetworkConnectType(IntEnum):
    NETWORK_CONNECT_TYPE_BEGIN = 0
    NETWORK_CONNECT_TYPE_EGO = 1
    NETWORK_CONNECT_TYPE_PUBSUB = 2
    NETWORK_CONNECT_TYPE_SIM = 3
    NETWORK_CONNECT_TYPE_END = 4

class TrafficLightColor(IntEnum) :
    TL_COLOR_BEGIN = 0
    TL_COLOR_R = 1				    # Red
    TL_COLOR_Y = 4				    # Yellow
    TL_COLOR_SG = 16				# Straigt Green >> 직진 녹색
    TL_COLOR_LG = 32				# Left    Green >> ← 좌회전 녹색
    TL_COLOR_RG = 64				# Right   Green >> → 우회전 녹색
    TL_COLOR_UTG = 128				# UTurn   Green 
    TL_COLOR_ULG = 256				# Upper Left  Green >> ↖
    TL_COLOR_URG = 512				# Upper Right Green >> ↗
    TL_COLOR_LLG = 1024				# Lower Left  Green >> ↙
    TL_COLOR_LRG = 2048				# Lower Right Green >> ↘ 
    
    TL_COLOR_R_WITH_Y = 5		    # R | Y
    TL_COLOR_Y_WITH_G = 20		    # Y | SG
    TL_COLOR_Y_WITH_GLEFT = 36		# Y | LG
    TL_COLOR_G_WITH_GLEFT = 48		# SG | LG
    TL_COLOR_R_WITH_GLEFT = 33		# R | LG
    TL_COLOR_LLG_SG = 1040		    # SG | LLG
    TL_COLOR_R_LLG = 1025		    # R | LLG
    TL_COLOR_ULG_URG = 768		    # ULG | URG

    TL_COLOR_NONE = 0               # 불이 꺼져있는 상태
    TL_COLOR_UNDEFINED = -1         # 신호등이 초기화 되지 않았을 때
    TL_COLOR_NOT_DETECTED = -2

class CruiseType(IntEnum):
    CRUISE_TYPE_BEGIN = 0
    CRUISE_TYPE_LINK = 1
    CRUISE_TYPE_CONSTANT = 2
    CRUISE_TYPE_END = 3


class VehicleType(IntEnum):
    VEHICLE_TYPE_UNKNOWN = 0
    VEHICLE_TYPE_MASTER = 1
    VEHICLE_TYPE_MULTI_EGO = 2
    VEHICLE_TYPE_SURROUND = 3

class ActorInfo:
    def __init__(self, role_name = '-1', actor_type = ActorType.ACTOR_TYPE_VEHICLE):
        self.role_name = role_name
        self.actor_type = actor_type

class BoundingBox:
    def __init__(self, extent=0, location=0, rotation=0):
        self.extent = extent
        self.location = location
        self.rotation = rotation


class LinkInfo:
    def __init__(self):
        self.unique_id = ''
        self.waypoint_idx = 0

class VehicleAuxState:
    def __init__(self):
        self.current_link_info = LinkInfo()
        self.remaining_distance = 0.0
        self.is_pass_dest_pos = False
        self.tl_id = ''
        self.tl_color = TrafficLightColor.TL_COLOR_BEGIN
        self.is_collision = False

class VehicleState:
    def __init__(self):
        self.throttle = 0.0
        self.steer = 0.0
        self.brake = 0.0
        self.front_wheel_angle = 0.0
        self.gear_mode = GearMode.GEAR_MODE_D
        self.vehicle_aux_state = VehicleAuxState()

class ActorState:
    def __init__(self):
        self.actor_info = ActorInfo()
        self.bounding_box = BoundingBox()
        self.transform = Transform()
        self.velocity = Vector3()
        self.angular_velocity = Vector3()
        self.acceleration = Vector3()
        
        self.vehicle_state = VehicleState()

    def get_current_lane_id(self):
        return self.vehicle_state.vehicle_aux_state.current_link_info.unique_id

class Vector3:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z


class Location(Vector3):
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, location):
        dest = np.array([location.x, location.y, location.z])
        src = np.array([self.x, self.y, self.z])
        vect = dest - src
        distance = np.linalg.norm(vect, ord=2)
        return distance

    def is_empty(self):
        return True if (self.x == 0 and self.y == 0 and self.z == 0) else False
        
    def get_dir_vector(self, location) :
        dest = np.array([location.x, location.y, location.z])
        src = np.array([self.x, self.y, self.z])
        dir_vec = dest - src
        norm_dir_vec = dir_vec / np.linalg.norm(dir_vec, ord=2)
        return norm_dir_vec


class Rotation:
    def __init__(self, roll = 0, pitch = 0, yaw = 0):
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def get_forward_vector(self):        
        vector = Vector3()        
        return vector

    def is_empty(self):
        return True if (self.roll == 0 and self.pitch == 0 and self.yaw == 0) else False


class Transform:
    def __init__(self, location=Location(), rotation=Rotation()):
        self.location = location
        self.rotation = rotation

    def is_empty(self):
        return True if (self.location.is_empty() and self.rotation.is_empty()) else False

    def calculate_rotation(self, target_transform : 'Transform') :
        '''해당 waypoint 를 바라보는 yaw값을 설정'''
        # norm_dir_vec = self.location.get_dir_vector(target_transform.location)
        target_pos = np.array([target_transform.location.x, target_transform.location.y, target_transform.location.z])
        cur_pos = np.array([self.location.x, self.location.y, self.location.z])

        dir_vec = target_pos - cur_pos
        norm_dir_vector = np.array([dir_vec[0], dir_vec[1], 0])
        norm_dir_vector = norm_dir_vector / np.linalg.norm(norm_dir_vector, ord=2)
        yaw_actan = np.math.atan2(norm_dir_vector[1], norm_dir_vector[0])
        yaw_deg = yaw_actan * (180 / np.pi)

        self.rotation.roll = 0
        self.rotation.pitch = 0
        self.rotation.yaw = yaw_deg

        return self

    def transform(self, transform : 'Transform'):
        world_tr = Transform()
        world2self_tr = get_tr(self) # 월드 좌표축 -> self 좌표축, self 좌표 -> 월드 좌표
        self2target_tr = get_tr(transform)
        world2target_tr = world2self_tr @ self2target_tr
        
        r = world2target_tr[:3, :3]
        rpy = r2rpy(r)
        world_tr.location.x, world_tr.location.y, world_tr.location.z = world2target_tr[:3, 3]
        world_tr.rotation.roll = rpy[0]
        world_tr.rotation.pitch = rpy[1]
        world_tr.rotation.yaw = rpy[2]

        return world_tr

    def get_transform_to(self, distance, ObjectParams : 'ObjectParams'):
        
        _g90_front = 4.02
        _model = ObjectParams.object_name
        _scale = ObjectParams.scale

        if _model == "OBJ_Hyundai_Grandeur":
            transform = Transform(Location(x=_g90_front+distance+_scale.x*1.12, y=0, z=_scale.z*0.34), Rotation(yaw=0))
        elif _model == "OBJ_Hyundai_Universe_High":
            transform = Transform(Location(x=_g90_front+distance+_scale.x*3.24, y=0, z=_scale.z*0.53), Rotation(yaw=0))
        elif _model == "OBJ_Hyundai_Sonata":
            transform = Transform(Location(x=_g90_front+distance+_scale.x*1.085, y=0, z=_scale.z*0.33), Rotation(yaw=0))
        elif _model == "SportBike":
            transform = Transform(Location(x=_g90_front+distance+_scale.x*0.815), Rotation(yaw=0))
        elif _model == "CargoBox":
            transform = Transform(Location(x=_g90_front+distance+_scale.x*0.375), Rotation(yaw=0))
        elif _model == "OBJ_Boy":
            transform = Transform(Location(x=_g90_front+distance+_scale.x*0.1), Rotation(yaw=0))
        elif _model == "OBJ_Man":
            transform = Transform(Location(x=_g90_front+distance+_scale.x*0.15), Rotation(yaw=0))
        elif _model == "Bike1":
            transform = Transform(Location(x=_g90_front+distance+_scale.x*0.825), Rotation(yaw=180))
        elif _model == "ChessboardObject":
            transform = Transform(Location(x=_g90_front+distance, y=0, z=1+_scale.z*0.75), Rotation(yaw=180))
        else:
            raise ValueError(f"{_model} does not exist.")
        
        return transform

class ObjectParams:
    def __init__(self):
        self.scale = None
        self.object_name = 'WoodBox'