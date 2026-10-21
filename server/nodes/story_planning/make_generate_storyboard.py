from server.model import TextModel
from server.states import ComicDramaState


def make_generate_storyboard(text_model: TextModel):
    """通过闭包注入文本模型"""

    # 闭包
    def generate_storyboard(state: ComicDramaState) -> dict[str, object]:
        requirement = state.get("requirement")
        outline = state.get("story_outline")
        characters = state.get("characters")
        scenes = state.get("scenes")

        if requirement is None or outline is None or not characters or not scenes:
            raise ValueError("缺少需求、大纲、角色或场景，不能生成分镜")

        storyboard = text_model.generate_storyboard(
            requirement, outline, characters, scenes
        )
        return {
            "storyboard": storyboard,
            "current_stage": "storyboard_generated",
            "events": ["已生成结构化分镜"],
        }

    return generate_storyboard
