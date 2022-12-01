import os, sys

current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.normpath(os.path.join(current_path, './')))
sys.path.append(os.path.normpath(os.path.join(current_path, '../')))

import grpc
import google.protobuf.empty_pb2
import protobuf.morai_actor_pb2
import protobuf.morai_actor_pb2_grpc
import protobuf.morai_mgeo_pb2
import protobuf.morai_mgeo_pb2_grpc
import protobuf.morai_sim_info_pb2
import protobuf.morai_sim_info_pb2_grpc
import protobuf.morai_simulation_pb2
import protobuf.morai_simulation_pb2_grpc
import protobuf.morai_sensor_pb2
import protobuf.morai_sensor_pb2_grpc
import protobuf.morai_type_pb2

import threading
from common_utils.compress_utils import decompress

MAX_MESSAGE_LENGTH = 33554432 # 32mb
DEFAULT_MORAI_SIM_IP = '127.0.0.1'
DEFAULT_MORAI_SIM_PORT = 7780

class SimAdapter():
    def __init__(self):
        self.__ip = DEFAULT_MORAI_SIM_IP
        self.__port = DEFAULT_MORAI_SIM_PORT
        self.__channel = None
        self.__actor_stub = None
        self.__mgeo_stub = None
        self.__sim_info_stub = None
        self.__simulation_stub = None
        self.__sensor_stub = None
        self.__actor_state_thread = None
        self.__on_actor_state_received_callback = None
        self.__actor_states = protobuf.morai_actor_pb2.ActorStates()
        self.__actor_state_recevier_stop_flag = False
        self.__actor_states_lock = threading.Lock()


    def get_ip(self):
        return self.__ip


    def get_port(self):
        return self.__port


    def is_connected(self):
        return False if (self.__channel == None) else True


    def connect(self, ip=DEFAULT_MORAI_SIM_IP, port=DEFAULT_MORAI_SIM_PORT):
        if self.is_connected():
            self.disconnect()

        self.__ip = ip
        self.__port = port

        self.__channel = grpc.insecure_channel(
            f'{self.__ip}:{self.__port}',
            options=[
                ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
            ]
        )
        # self.channel = grpc.insecure_channel(f'{self.ip}:{self.port}')
        self.__actor_stub = protobuf.morai_actor_pb2_grpc.MoraiActorStub(self.__channel)
        self.__mgeo_stub = protobuf.morai_mgeo_pb2_grpc.MoraiMgeoStub(self.__channel)
        self.__sim_info_stub = protobuf.morai_sim_info_pb2_grpc.MoraiSimInfoStub(self.__channel)
        self.__simulation_stub = protobuf.morai_simulation_pb2_grpc.MoraiSimulationStub(self.__channel)
        self.__sensor_stub = protobuf.morai_sensor_pb2_grpc.MoraiSensorStub(self.__channel)
        

    def disconnect(self):
        if not self.is_connected():
            return

        try:
            self.__channel.close()
            self.__channel = None

            self.__actor_stub = None
            self.__mgeo_stub = None
            self.__sim_info_stub = None
            self.__simulation_stub = None

            self.__actor_state_recevier_stop_flag = True
            if self.__actor_state_thread != None:
                self.__actor_state_thread.join()

        except BaseException as e:
            print(e)


    def initialize(self):
        try:
            request = google.protobuf.empty_pb2.Empty()
            self.__simulation_stub.Initialize(request)
        except BaseException as e:
            print(f'initialize failed : {e}')


    def get_simulator_version(self):
        simulator_version = ""
        try:
            request = google.protobuf.empty_pb2.Empty()
            response = self.__sim_info_stub.GetSimulatorVersion(request)
            simulator_version = response.value
        except Exception as e:
            print(f'get_simulator_version failed : {e}')
        return simulator_version


    def get_available_maps(self):
        available_maps = []
        try:
            request = google.protobuf.empty_pb2.Empty()
            response = self.__sim_info_stub.GetAvailableMaps(request)
            available_maps = response.values
        except Exception as e:
            print(f'get_available_maps failed : {e}')

        return available_maps


    def get_data_path(self):
        data_path = ''
        try:
            request = google.protobuf.empty_pb2.Empty()
            response = self.__sim_info_stub.GetDataPath(request)
            data_path = response.value
        except Exception as e:
            print(f'get_Data_path failed : {e}')

        return data_path


    def get_actor_types(self):
        actor_types = [
            protobuf.morai_actor_pb2.ACTOR_TYPE_UNKNOWN,
            protobuf.morai_actor_pb2.ACTOR_TYPE_VEHICLE,
            protobuf.morai_actor_pb2.ACTOR_TYPE_PEDESTRIAN,
            protobuf.morai_actor_pb2.ACTOR_TYPE_OBSTACLE]

        return actor_types


    def set_ego(self, ego_ctrl_cmd):
        try:
            response = self.__actor_stub.SetEgo(ego_ctrl_cmd)
            return response.success
        except Exception as e:
            print(f'ego ctrl failed : {e}')


    def load_world(self, map_name, ego_vehicle_model):
        try:
            request = protobuf.morai_simulation_pb2.LoadWorldParam()
            request.map_name = map_name
            request.ego_vehicle_model = ego_vehicle_model
            request.wait = True
            response = self.__simulation_stub.LoadWorld(request)
            if not response.success:
                print(f'load world result : {response.description}')
        except Exception as e:
            print(f'load_map failed : {e}')
            return False

        return True


    def ray_cast(self, raycast_param):
        occlusion_dist = -1.0
        try:
            response = self.__simulation_stub.RayCast(raycast_param)
            occlusion_dist = response.value
        except Exception as e:
            print(f'ray_cast failed : {e}')

        return occlusion_dist


    def spawn_actor(self, spawn_actor_param):        
        actor_responses = None
        try:            
            actor_responses = self.__actor_stub.SpawnActor(spawn_actor_param)
        except Exception as e:
            print(f'spawn_actor failed : {e}')

        return actor_responses


    def vehicle_control(self, vehicle_ctrl_cmd):
        result = False
        try:
            response = self.__actor_stub.VehicleControl(vehicle_ctrl_cmd)
            result = response.success
        except Exception as e:
            print(f'vehicle_control failed : {e}')

        return result


    def destroy_actor(self, actor_info):
        try:
            response = self.__actor_stub.DestroyActor(actor_info)
            # print("destroy_actor result {}".format(response.success))
        except Exception as e:
            print(f'destroy_actor failed : {e}')


    def destroy_all_actors(self):
        try:
            response = self.__actor_stub.DestroyAllActors(google.protobuf.empty_pb2.Empty())
            # print(f'destroy_all_actors result {response.success}')
        except Exception as e:
            print(f'destroy_all_actors failed : {e}')


    def get_timestamp(self):
        sim_timestamp = -1
        try:
            response = self.__sim_info_stub.GetTimestamp(google.protobuf.empty_pb2.Empty())
            sim_timestamp = response.value
        except Exception as e:
            print("get_timestamp failed : ", e)

        return sim_timestamp


    def get_weather(self):
        weather = protobuf.morai_simulation_pb2.WEATHER_TYPE_SUNNY        
        try:
            response = self.__simulation_stub.GetWeather(google.protobuf.empty_pb2.Empty())
            weather = response.weather_type
        except Exception as e:
            print("get_weather failed : ", e)
        
        return weather


    def set_weather(self, weather_type):
        request = protobuf.morai_simulation_pb2.WeatherParam()
        request.weather_type = weather_type
        try:
            self.__simulation_stub.SetWeather(request)
        except Exception as e:
            print("set_weather failed : ", e)


    def pause(self):
        result = False
        try:
            response = self.__simulation_stub.Pause(google.protobuf.empty_pb2.Empty())
            result = response.success
        except Exception as e:
            print("pause failed : ", e)
            
        return result


    def resume(self):
        result = False
        try:
            response = self.__simulation_stub.Resume(google.protobuf.empty_pb2.Empty())
            result = response.success
        except Exception as e:
            print("resume failed : ", e)
            
        return result


    def is_synchronous_mode(self):
        enabled = False
        try:
            result = self.__simulation_stub.IsSynchronousMode(google.protobuf.empty_pb2.Empty())
            enabled = result.value
        except Exception as e:
            print("is_synchronous_mode failed : ", e)
            
        return enabled


    def set_synchronous_mode(self, enabled):
        result = False
        try:
            request = protobuf.morai_type_pb2.BoolValue()
            request.value = enabled

            response = self.__simulation_stub.SetSynchronousMode(request)
            result = response.success
        except Exception as e:
            print("set_synchronous_mode failed : ", e)

        return result


    def tick(self, elapse_time):
        result = False
        try:
            request = protobuf.morai_type_pb2.Int32Value()
            request.value = elapse_time

            response = self.__simulation_stub.Tick(request)
            result = response.value
        except Exception as e:
            print("tick failed : ", e)

        return result


    def wait_for_tick(self):
        sim_timestamp = -1
        try:
            request = google.protobuf.empty_pb2.Empty()
            response = self.__simulation_stub.WaitForTick(request)
            sim_timestamp = response.value
        except Exception as e:
            print("wait_for_tick failed : ", e)

        return sim_timestamp


    def get_mgeo(self, map_name):
        mgeo_data = None
        try:
            request = protobuf.morai_mgeo_pb2.MapInfo()
            request.map_name = map_name

            mgeo_data = self.__mgeo_stub.GetMGeo(request)
            self.decompress_mgeo(mgeo_data)

        except Exception as e:
            print("get_mgeo failed : ", e)

        return mgeo_data


    def start_actor_state_receiver(self, on_received_callback = None):
        self.__actor_state_recevier_stop_flag = False
        self.__on_actor_state_received_callback = on_received_callback
        self.__actor_state_thread = threading.Thread(target=self.receive_actor_state, args=(lambda: self.__actor_state_recevier_stop_flag, ))
        self.__actor_state_thread.start()


    def receive_actor_state(self, stop):
        self.__actor_state_channel = grpc.insecure_channel(f'{self.__ip}:{self.__port}')
        self.__actor_state_stub = protobuf.morai_actor_pb2_grpc.MoraiActorStub(self.__actor_state_channel)

        result = None
        while result is None:
            try:
                actor_state_stream = self.__actor_state_stub.GetActorStateStream(google.protobuf.empty_pb2.Empty())
                for actor_states in actor_state_stream:
                    self.__actor_states_lock.acquire()
                    self.__actor_states.CopyFrom(actor_states)
                    self.__actor_states_lock.release()
                    if self.__on_actor_state_received_callback != None:
                        self.__on_actor_state_received_callback()

                    if stop():
                        actor_state_stream.cancel()
                        break
                result = True
                break
            except:
                print("actor_state_stream is empty. Trying again")
                pass


    def get_actor_state(self, actor_info):
            actor_state = None
            try:
                actor_state = self.__actor_stub.GetActorState(actor_info)
            except Exception as e:
                print(f'get_actor_state failed : {e}')

            return actor_state

    def set_actor_property(self, actor_property):
        success = False
        try:
            response = self.__actor_stub.SetActorProperty(actor_property)
            success = response.success
        except Exception as e:
            print(f'set actor property failed : {e}')

        return success


    def get_actor_network_config(self, actor_info):
        response = None
        try:
            response = self.__actor_stub.GetActorNetworkSetting(actor_info)
        except Exception as e:
            print(f'get actor network config failed : {e}')
        
        return response


    def get_traffic_light_info_by_link(self, link_info):
        tl_info = None
        try:
            tl_info = self.__actor_stub.GetTrafficLightInfoByLink(link_info)
        except BaseException as e:
            print(f'get_traffic_light_info_by_link failed : {e}')

        return tl_info


    def get_traffic_light_info_by_uid(self, traffic_light_id):
        tl_info = None
        try:
            tl_info = self.__actor_stub.GetTrafficLightInfoByUid(traffic_light_id)
        except BaseException as e:
            print(f'get_traffic_light_info_by_uid failed : {e}')

        return tl_info


    def get_intscn_tl_info(self, intscn_id):
        tl_info_list = None
        try:
            tl_info_list = self.__actor_stub.GetIntscnTLInfo(intscn_id)
        except BaseException as e:
            print(f'get_intscn_tl_info failed : {e}')

        return tl_info_list


    def set_traffic_light_state(self, traffic_light_states):
        actor_responses = None
        try:
            actor_responses = self.__actor_stub.SetTrafficLightState(traffic_light_states)
        except BaseException as e:
            print(f'set traffic light state failed : {e}')

        return actor_responses


    def set_intersection_state(self, intersection_param_list):
        try:
            response = self.__actor_stub.SetIntersectionState(intersection_param_list)
            return response
        except BaseException as e:
            return

    def set_intersection_schedule(self, intersection_schedule_list):
        try:
            response = self.__actor_stub.SetIntersectionSchedule(intersection_schedule_list)
            return response
        except BaseException as e:
            return

    def set_vehicle_route(self, vehicle_route):
        try:
            response = self.__actor_stub.SetVehicleRoute(vehicle_route)
            print(f'route response : {response.description}')
            return response
        except BaseException as e:
            print(f'route exception : {e}')
            return

    def set_vehicle_destination(self, vehicle_destination):
        try:
            response = self.__actor_stub.SetVehicleDestination(vehicle_destination)
            print(f'set vehicle destination : {response.description}')
            return response
        except BaseException as e:
            print(f'set vehicle destination exception : {e}')

    def add_sensor(self, sensor_setting_list):
        try:
            response = self.__sensor_stub.AddSensor(sensor_setting_list)
            return response
        except BaseException as e:
            print(f'add sensor exception : {e}')

    def remove_sensor(self, remove_sensor_list):
        try:
            response = self.__sensor_stub.RemoveSensor(remove_sensor_list)
            return response
        except BaseException as e:
            print(f'remove sensor exception : {e}')

    def set_gt_sensor(self, set_gt_sensor_list):
        try:
            response = self.__sensor_stub.SetGroundTruthSensor(set_gt_sensor_list)
            return response
        except BaseException as e:
            print(f'set gt sensor exception : {e}')        

    def get_gt_data(self, target_sensor_list):
        try:
            response = self.__sensor_stub.GetGroundTruthData(target_sensor_list)
            return response
        except BaseException as e:
            print(f'get gt data exception : {e}')  

    def save_sensor_data(self, save_sensor_data):
        try:
            self.__sensor_stub.SaveSensorData(save_sensor_data)
        except BaseException as e:
            print(f'save sensor data exception : {e}')
            
    def load_sensor_file(self, sensor_filename):
        try:
            request = protobuf.morai_type_pb2.StringValue()
            request.value = sensor_filename
            response = self.__sensor_stub.LoadSensorFile(request)
            return response
        except BaseException as e:
            print(f'load sensor file exception : {e}')

    def decompress_mgeo(self, mgeo_data):
        mgeo_data.global_info = decompress(mgeo_data.global_info)
        mgeo_data.lane_marking_set = decompress(mgeo_data.lane_marking_set)
        mgeo_data.lane_node_set = decompress(mgeo_data.lane_node_set)
        mgeo_data.linke_set = decompress(mgeo_data.linke_set)
        mgeo_data.node_set = decompress(mgeo_data.node_set)
        mgeo_data.traffic_light_set = decompress(mgeo_data.traffic_light_set)
        mgeo_data.intersection_controller_set = decompress(mgeo_data.intersection_controller_set)
        mgeo_data.intersection_controller_data = decompress(mgeo_data.intersection_controller_data)
