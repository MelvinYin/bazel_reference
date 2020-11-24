import os
from python_folder import grpc_service_pb2, grpc_service_pb2_grpc
import grpc
from concurrent import futures

class Server(grpc_service_pb2_grpc.TicServicer):
    def sendTic(self, request, context):
        print(request)
        returned = grpc_service_pb2.Results(result=[1, 2, 3, 4, 5])
        context.set_code(grpc.StatusCode.OK)
        return returned

def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1),
                         maximum_concurrent_rpcs=1)
    grpc_service_pb2_grpc.add_TicServicer_to_server(Server(), server)
    address = '{}:{}'.format('localhost', 8012)
    actual_port = server.add_insecure_port(address)
    server.start()
    server.wait_for_termination()

start_server()