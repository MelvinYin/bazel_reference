from python_folder import grpc_service_pb2, grpc_service_pb2_grpc
import grpc

def ping(portno):
    print(f"AdminPage.ping called.")
    with grpc.insecure_channel(f'localhost:{portno}') as channel:
        stub = grpc_service_pb2_grpc.TicStub(channel)
        request_object = grpc_service_pb2.SelectionObject(select=123)
        return_object = stub.sendTic(request_object)
        print(type(return_object))
        for term in return_object.result:
            print(term)
        print(return_object)
    print(f"AdminPage.ping completed.\n")


ping(8012)