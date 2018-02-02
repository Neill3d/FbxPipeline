# automatically generated by the FlatBuffers compiler, do not modify

# namespace: apemodefb

import flatbuffers

class PackedSkinnedVertexFb(object):
    __slots__ = ['_tab']

    # PackedSkinnedVertexFb
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PackedSkinnedVertexFb
    def Position(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # PackedSkinnedVertexFb
    def Normal(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # PackedSkinnedVertexFb
    def Tangent(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # PackedSkinnedVertexFb
    def Uv(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(12))
    # PackedSkinnedVertexFb
    def Weights(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16))
    # PackedSkinnedVertexFb
    def Indices(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(20))

def CreatePackedSkinnedVertexFb(builder, position, normal, tangent, uv, weights, indices):
    builder.Prep(4, 24)
    builder.PrependUint32(indices)
    builder.PrependUint32(weights)
    builder.PrependUint32(uv)
    builder.PrependUint32(tangent)
    builder.PrependUint32(normal)
    builder.PrependUint32(position)
    return builder.Offset()