# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from eth.v1alpha1 import node_pb2 as eth_dot_v1alpha1_dot_node__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class NodeStub(object):
    """Node service API

    Node service provides general information about the node itself, the services
    it supports, chain information and node version.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSyncStatus = channel.unary_unary(
                '/ethereum.eth.v1alpha1.Node/GetSyncStatus',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=eth_dot_v1alpha1_dot_node__pb2.SyncStatus.FromString,
                )
        self.GetGenesis = channel.unary_unary(
                '/ethereum.eth.v1alpha1.Node/GetGenesis',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=eth_dot_v1alpha1_dot_node__pb2.Genesis.FromString,
                )
        self.GetVersion = channel.unary_unary(
                '/ethereum.eth.v1alpha1.Node/GetVersion',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=eth_dot_v1alpha1_dot_node__pb2.Version.FromString,
                )
        self.ListImplementedServices = channel.unary_unary(
                '/ethereum.eth.v1alpha1.Node/ListImplementedServices',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=eth_dot_v1alpha1_dot_node__pb2.ImplementedServices.FromString,
                )
        self.GetHost = channel.unary_unary(
                '/ethereum.eth.v1alpha1.Node/GetHost',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=eth_dot_v1alpha1_dot_node__pb2.HostData.FromString,
                )
        self.GetPeer = channel.unary_unary(
                '/ethereum.eth.v1alpha1.Node/GetPeer',
                request_serializer=eth_dot_v1alpha1_dot_node__pb2.PeerRequest.SerializeToString,
                response_deserializer=eth_dot_v1alpha1_dot_node__pb2.Peer.FromString,
                )
        self.ListPeers = channel.unary_unary(
                '/ethereum.eth.v1alpha1.Node/ListPeers',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=eth_dot_v1alpha1_dot_node__pb2.Peers.FromString,
                )


class NodeServicer(object):
    """Node service API

    Node service provides general information about the node itself, the services
    it supports, chain information and node version.
    """

    def GetSyncStatus(self, request, context):
        """Retrieve the current network sync status of the node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGenesis(self, request, context):
        """Retrieve information about the genesis of Ethereum 2.0.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVersion(self, request, context):
        """Retrieve information about the running Ethereum 2.0 node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListImplementedServices(self, request, context):
        """Retrieve the list of services implemented and enabled by this node.

        Any service not present in this list may return UNIMPLEMENTED or
        PERMISSION_DENIED. The server may also support fetching services by grpc
        reflection.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHost(self, request, context):
        """Retrieves the peer data of the local peer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPeer(self, request, context):
        """Retrieve the peer corresponding to the provided peer id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPeers(self, request, context):
        """Retrieve the list of peers currently connected to this node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSyncStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSyncStatus,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=eth_dot_v1alpha1_dot_node__pb2.SyncStatus.SerializeToString,
            ),
            'GetGenesis': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGenesis,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=eth_dot_v1alpha1_dot_node__pb2.Genesis.SerializeToString,
            ),
            'GetVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVersion,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=eth_dot_v1alpha1_dot_node__pb2.Version.SerializeToString,
            ),
            'ListImplementedServices': grpc.unary_unary_rpc_method_handler(
                    servicer.ListImplementedServices,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=eth_dot_v1alpha1_dot_node__pb2.ImplementedServices.SerializeToString,
            ),
            'GetHost': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHost,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=eth_dot_v1alpha1_dot_node__pb2.HostData.SerializeToString,
            ),
            'GetPeer': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPeer,
                    request_deserializer=eth_dot_v1alpha1_dot_node__pb2.PeerRequest.FromString,
                    response_serializer=eth_dot_v1alpha1_dot_node__pb2.Peer.SerializeToString,
            ),
            'ListPeers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPeers,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=eth_dot_v1alpha1_dot_node__pb2.Peers.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ethereum.eth.v1alpha1.Node', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Node(object):
    """Node service API

    Node service provides general information about the node itself, the services
    it supports, chain information and node version.
    """

    @staticmethod
    def GetSyncStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethereum.eth.v1alpha1.Node/GetSyncStatus',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            eth_dot_v1alpha1_dot_node__pb2.SyncStatus.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGenesis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethereum.eth.v1alpha1.Node/GetGenesis',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            eth_dot_v1alpha1_dot_node__pb2.Genesis.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethereum.eth.v1alpha1.Node/GetVersion',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            eth_dot_v1alpha1_dot_node__pb2.Version.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListImplementedServices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethereum.eth.v1alpha1.Node/ListImplementedServices',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            eth_dot_v1alpha1_dot_node__pb2.ImplementedServices.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethereum.eth.v1alpha1.Node/GetHost',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            eth_dot_v1alpha1_dot_node__pb2.HostData.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPeer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethereum.eth.v1alpha1.Node/GetPeer',
            eth_dot_v1alpha1_dot_node__pb2.PeerRequest.SerializeToString,
            eth_dot_v1alpha1_dot_node__pb2.Peer.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPeers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethereum.eth.v1alpha1.Node/ListPeers',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            eth_dot_v1alpha1_dot_node__pb2.Peers.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
