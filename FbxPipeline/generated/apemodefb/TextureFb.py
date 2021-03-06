# automatically generated by the FlatBuffers compiler, do not modify

# namespace: apemodefb

import flatbuffers

class TextureFb(object):
    __slots__ = ['_tab']

    # TextureFb
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TextureFb
    def Id(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # TextureFb
    def NameId(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # TextureFb
    def FileId(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # TextureFb
    def TextureTypeId(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(12))
    # TextureFb
    def BlendMode(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16))
    # TextureFb
    def WrapModeU(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(20))
    # TextureFb
    def WrapModeV(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(24))
    # TextureFb
    def OffsetU(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(28))
    # TextureFb
    def OffsetV(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(32))
    # TextureFb
    def ScaleU(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(36))
    # TextureFb
    def ScaleV(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(40))
    # TextureFb
    def CroppingBottom(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(44))
    # TextureFb
    def CroppingLeft(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(48))
    # TextureFb
    def CroppingRight(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(52))
    # TextureFb
    def CroppingTop(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(56))
    # TextureFb
    def RotationU(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(60))
    # TextureFb
    def RotationV(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(64))
    # TextureFb
    def RotationW(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(68))
    # TextureFb
    def SwapUv(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(72))
    # TextureFb
    def WipeMode(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(73))
    # TextureFb
    def PremultipliedAlpha(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(74))
    # TextureFb
    def AlphaSource(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(76))
    # TextureFb
    def TextureUse(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(80))
    # TextureFb
    def MappingType(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(84))
    # TextureFb
    def PlanarMappingNormal(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(88))

def CreateTextureFb(builder, id, nameId, fileId, textureTypeId, blendMode, wrapModeU, wrapModeV, offsetU, offsetV, scaleU, scaleV, croppingBottom, croppingLeft, croppingRight, croppingTop, rotationU, rotationV, rotationW, swapUv, wipeMode, premultipliedAlpha, alphaSource, textureUse, mappingType, planarMappingNormal):
    builder.Prep(4, 92)
    builder.PrependUint32(planarMappingNormal)
    builder.PrependUint32(mappingType)
    builder.PrependUint32(textureUse)
    builder.PrependUint32(alphaSource)
    builder.Pad(1)
    builder.PrependBool(premultipliedAlpha)
    builder.PrependBool(wipeMode)
    builder.PrependBool(swapUv)
    builder.PrependFloat32(rotationW)
    builder.PrependFloat32(rotationV)
    builder.PrependFloat32(rotationU)
    builder.PrependInt32(croppingTop)
    builder.PrependInt32(croppingRight)
    builder.PrependInt32(croppingLeft)
    builder.PrependInt32(croppingBottom)
    builder.PrependFloat32(scaleV)
    builder.PrependFloat32(scaleU)
    builder.PrependFloat32(offsetV)
    builder.PrependFloat32(offsetU)
    builder.PrependUint32(wrapModeV)
    builder.PrependUint32(wrapModeU)
    builder.PrependUint32(blendMode)
    builder.PrependUint32(textureTypeId)
    builder.PrependUint32(fileId)
    builder.PrependUint32(nameId)
    builder.PrependUint32(id)
    return builder.Offset()
