from moraikit.protobuf.conversions import from_actor_state_msg, to_transform_msg, to_vector3_msg
from moraikit.types import ObjectParams, Transform, Vector3
from moraikit.sim_adapter import SimAdapter
import moraikit.protobuf.morai_actor_pb2
import protobuf.morai_type_pb2
import protobuf.morai_actor_pb2
import google.protobuf.empty_pb2
from protobuf.morai_sensor_pb2 import SENSOR_TYPE_CAMERA, SaveSensor, SensorSetting, SensorSettingList, RemoveSensor, RemoveSensorList
from copy import deepcopy as dc

DEFAULT_MORAI_SIM_IP = '127.0.0.1'
DEFAULT_MORAI_SIM_PORT = 7780

class SensorApi(SimAdapter):

    def connect(self, ip=DEFAULT_MORAI_SIM_IP, port=DEFAULT_MORAI_SIM_PORT):
        return super().connect(ip, port)      

    def disconnect(self):
        return super().disconnect()

    def initialize(self):
        return super().initialize()

    def get_ip(self):
        return super().get_ip()

    def get_port(self):
        return super().get_port()

    def is_connected(self):
        return super().is_connected()

    def get_simulator_version(self):
        return super().get_simulator_version()

    def get_available_objects(self):
        available_objects = []
        try:
            request = google.protobuf.empty_pb2.Empty()
            response = super().__sim_info_stub.GetAvailableObject(request)
            available_objects = response.values
        except Exception as e:
            print(f'get_available_objects failed : {e}')
        return available_objects

    def get_available_maps(self):
        return super().get_available_maps()
    
    def get_data_path(self):
        return super().get_data_path()

    def get_ego_transform(self):
        return self.get_actor_state('0').transform

    def load_world(self, map_name, ego_name='2017_Kia_Niro(HEV)'):
        return super().load_world(map_name, ego_name)

    # def spawn_object(self, transform, obj_params=ObjectParams()):
    #     spawn_actor_params = protobuf.morai_actor_pb2.SpawnActorParams()
    #     param = protobuf.morai_actor_pb2.SpawnActorParam()        
    #     param.actor_info.actor_id = '-1'
    #     param.actor_info.actor_type = moraikit.protobuf.morai_actor_pb2.ACTOR_TYPE_OBSTACLE
        
    #     to_transform_msg(param.transform, transform)

    #     if obj_params.scale is None:
    #         obj_params.scale = Vector3(1.0, 1.0, 1.0)
    #     _obj_params = dc(obj_params)            
    #     _obj_params.scale.x = obj_params.scale.y
    #     _obj_params.scale.y = obj_params.scale.z
    #     _obj_params.scale.z = obj_params.scale.x       
    #     to_vector3_msg(param.obstacle.scale, _obj_params.scale)
    #     param.obstacle.obstacle_name = obj_params.object_name

    #     spawn_actor_params.params.append(param)
    #     response = super().spawn_actor(spawn_actor_params)
        
    #     return self.extract_role_name(response)

    def spawn_object(self, distance, obj_params=ObjectParams()):
        spawn_actor_params = protobuf.morai_actor_pb2.SpawnActorParams()
        param = protobuf.morai_actor_pb2.SpawnActorParam()        
        param.actor_info.actor_id = '-1'
        param.actor_info.actor_type = moraikit.protobuf.morai_actor_pb2.ACTOR_TYPE_OBSTACLE
        
        _ego_transform = self.get_ego_transform()
        object_transform = _ego_transform.get_transform_to(distance, obj_params)
        transform = _ego_transform.transform(object_transform)

        to_transform_msg(param.transform, transform)

        if obj_params.scale is None:
            obj_params.scale = Vector3(1.0, 1.0, 1.0)
        _obj_params = dc(obj_params)            
        _obj_params.scale.x = obj_params.scale.y
        _obj_params.scale.y = obj_params.scale.z
        _obj_params.scale.z = obj_params.scale.x       
        to_vector3_msg(param.obstacle.scale, _obj_params.scale)
        param.obstacle.obstacle_name = obj_params.object_name

        spawn_actor_params.params.append(param)
        response = super().spawn_actor(spawn_actor_params)
        
        return self.extract_role_name(response)

    def spawn_object_from_camera(self, obj_id = '-1', camera_transform:Transform=None, obj_transform:Transform=None, obj_params=ObjectParams()):
        spawn_actor_params = protobuf.morai_actor_pb2.SpawnActorParams()
        param = protobuf.morai_actor_pb2.SpawnActorParam()        
        param.actor_info.actor_id = obj_id
        param.actor_info.actor_type = moraikit.protobuf.morai_actor_pb2.ACTOR_TYPE_OBSTACLE
        ego_transform = self.get_ego_transform()
        transform = ego_transform.transform(camera_transform.transform(obj_transform))
        to_transform_msg(param.transform, transform)

        if obj_params.scale is None:
            obj_params.scale = Vector3(1.0, 1.0, 1.0)
        _obj_params = dc(obj_params)            
        _obj_params.scale.x = obj_params.scale.y
        _obj_params.scale.y = obj_params.scale.z
        _obj_params.scale.z = obj_params.scale.x
        to_vector3_msg(param.obstacle.scale, _obj_params.scale)
        param.obstacle.obstacle_name = obj_params.object_name

        spawn_actor_params.params.append(param)
        response = super().spawn_actor(spawn_actor_params)
        
        return self.extract_role_name(response)

    def remove_object(self, object_id):
        param = protobuf.morai_actor_pb2.SpawnActorParam()        
        param.actor_info.actor_id = object_id
        param.actor_info.actor_type = moraikit.protobuf.morai_actor_pb2.ACTOR_TYPE_OBSTACLE
        
        self.destroy_actor(param.actor_info)
        return

    def set_camera(self, transform:Transform=None):
        # data -> proto
        request = SensorSettingList()
        
        msg = SensorSetting()
        msg.unique_id = '0' # 차량 ID
        msg.sensor_type = SENSOR_TYPE_CAMERA
        msg.position.x = transform.location.x
        msg.position.y = transform.location.y
        msg.position.z = transform.location.z
        msg.rotation.x = transform.rotation.roll
        msg.rotation.y = transform.rotation.pitch
        msg.rotation.z = transform.rotation.yaw

        request.req_list.append(msg)

        response = super().add_sensor(request)
        return response        
        
    def capture_data(self): 
        request = SaveSensor()
        request.is_custom_file_name = False
        super().save_sensor_data(request)

    def capture_data_custom(self, file_name:str="sample", file_dir:str="sample"):
        """파일 위치 및 이름 설정"""
        request = SaveSensor()
        request.is_custom_file_name = True
        request.custrom_file_name = file_name
        request.file_dir = file_dir
        super().save_sensor_data(request)

    def remove_camera(self, sensor_id):
        # data -> proto
        request = RemoveSensorList()
        
        msg = RemoveSensor()
        msg.unique_id = '0'
        msg.sensor_id = str(sensor_id)

        request.req_list.append(msg)
        
        response = super().remove_sensor(request)
        return response

    def load_sensor_preset(self, file_name):
        response = super().load_sensor_file(file_name)
        return response

    def get_actor_state(self, actor_id):
        actor_info = moraikit.protobuf.morai_actor_pb2.ActorInfo()
        actor_info.actor_id = actor_id
        actor_info.actor_type = moraikit.protobuf.morai_actor_pb2.ACTOR_TYPE_VEHICLE
        actor_state = super().get_actor_state(actor_info)
        conv_actor_state = from_actor_state_msg(actor_state)   

        return conv_actor_state


    """ Helper methods """
    def extract_role_name(self, actor_responses):
        role_name = ''
        if actor_responses == None or actor_responses.values[0].result == False:
            print('spawn actor error')
        else:
            role_name = actor_responses.values[0].display_name
        
        return role_name

