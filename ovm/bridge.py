from typing import Any, Iterable
import eth_abi
from eth_typing import TypeStr
import grpc
import bridge_pb2
import bridge_pb2_grpc


class Bridge:
    def __init__(self):
        self.bridge_client = bridge_pb2_grpc.BridgeStub(grpc.insecure_channel("unix:///var/run/ovm.sock"))

    def load(self):
        return self.bridge_client.Load(bridge_pb2.LoadRequest())

    def log(self, content: str):
        return self.bridge_client.Log(bridge_pb2.LogRequest(content=content))

    def submit(self, abi: Iterable[TypeStr], values: Iterable[Any]):
        return self.bridge_client.Submit(bridge_pb2.SubmitRequest(output=eth_abi.encode(abi, values).hex()))
