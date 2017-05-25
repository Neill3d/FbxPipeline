//#include <GameEngine.GraphicsEcosystem.Precompiled.h>
#include <Texture.Vulkan.h>

#include <CommandQueue.Vulkan.h>

/// -------------------------------------------------------------------------------------------------------------------
/// TextureResourceView
/// -------------------------------------------------------------------------------------------------------------------

std::shared_ptr<Core::TextureResourceView> Core::TextureResourceView::MakeNewLinked ()
{
    return std::shared_ptr<TextureResourceView> (new TextureResourceView ());
}

std::unique_ptr<Core::TextureResourceView> Core::TextureResourceView::MakeNewUnique ()
{
    return std::unique_ptr<TextureResourceView> (new TextureResourceView ());
}

Core::TextureResourceView::TextureResourceView ()
    : bIsCube (false)
    , Width (0)
    , Height (0)
    , ArrayLayerCount (0)
    , MipLevelCount (1)
    , Format (VK_FORMAT_UNDEFINED)
    , ImgUsage (VK_IMAGE_USAGE_SAMPLED_BIT)
    , ImgAspect (VK_IMAGE_ASPECT_COLOR_BIT)
    , ImgTiling (VK_IMAGE_TILING_OPTIMAL)
    , ImgViewType (VK_IMAGE_VIEW_TYPE_2D)
    , SampleCount (VK_SAMPLE_COUNT_1_BIT)
{
    ViewType = kResourceViewType_Texture;
}

void Core::TextureResourceView::SetState(Core::CommandList &  CmdList,
                                         VkPipelineStageFlags PipelineStageFlags,
                                         VkAccessFlags        AccessMask,
                                         VkImageLayout        ImgLayout,
                                         uint32_t             BaseMipLevel,
                                         uint32_t             MipLevelCount,
                                         uint32_t             BaseArrayLayer,
                                         uint32_t             ArrayLayerCount,
                                         uint32_t             QueueFamily)
{
    const auto StateIt = MemoryStates.find(&CmdList);
    const MemoryState & State = StateIt != MemoryStates.end()
                              ? StateIt->second
                              : MemoryStates[nullptr];

    if (_Game_engine_Likely (State.AccessMask != AccessMask
                             || State.ImgLayout != ImgLayout
                             || State.QueueFamily != QueueFamily
                             || State.PipelineStageFlags != PipelineStageFlags
                             || State.ImgSubresRange.aspectMask != ImgAspect
                             || State.ImgSubresRange.baseMipLevel != BaseMipLevel
                             || State.ImgSubresRange.levelCount != MipLevelCount
                             || State.ImgSubresRange.baseArrayLayer != BaseArrayLayer
                             || State.ImgSubresRange.layerCount != ArrayLayerCount))
    {
        TInfoStruct<VkImageMemoryBarrier> ImgBarrier;
        ImgBarrier->image                           = ImgHandle;
        ImgBarrier->oldLayout                       = State.ImgLayout;
        ImgBarrier->newLayout                       = ImgLayout;
        ImgBarrier->srcAccessMask                   = State.AccessMask;
        ImgBarrier->dstAccessMask                   = AccessMask;
        ImgBarrier->srcQueueFamilyIndex             = State.QueueFamily;
        ImgBarrier->dstQueueFamilyIndex             = QueueFamily;
        ImgBarrier->subresourceRange.aspectMask     = ImgAspect;
        ImgBarrier->subresourceRange.baseArrayLayer = BaseArrayLayer;
        ImgBarrier->subresourceRange.baseMipLevel   = BaseMipLevel;
        ImgBarrier->subresourceRange.layerCount     = ArrayLayerCount;
        ImgBarrier->subresourceRange.levelCount     = MipLevelCount;

        CmdList.InsertBarrier (State.PipelineStageFlags,
                               PipelineStageFlags,
                               ImgBarrier);

        ResourceView::SetState (CmdList,
                                MemoryState (PipelineStageFlags,
                                             AccessMask,
                                             QueueFamily,
                                             ImgLayout,
                                             ImgBarrier->subresourceRange));
    }
}

Core::TextureResourceView::~TextureResourceView()
{
}