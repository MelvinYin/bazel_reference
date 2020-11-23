//
//package grpc_tic_tac_toe;
//
//import plushie_tycoon.host.hostEngine.HostEngine;
//
//public class ClientPageService extends ClientPageGrpc.ClientPageImplBase  {
//    ClientEngine ge;
//    public ClientPageService(ClientEngine ge){
//        this.ge = ge;
//    }
//    @Override
//    public void buy(Grpc.TransactionObject request, StreamObserver<Grpc.Snapshot> responseObserver) {
//        System.out.println("ClientPageService.buy called");
//        Grpc.Snapshot output = ge.buy(BaseStringConverter.convert(request.getName()), request.getQuantity());
//        responseObserver.onNext(output);
//        responseObserver.onCompleted();
//    }
