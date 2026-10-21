from server.model import TextModel
from server.states import ComicDramaState


def make_generate_characters(text_model: TextModel):
    """通过闭包注入文本模型"""

    # 闭包
    def generate_characters(state: ComicDramaState) -> dict[str, object]:
        # 故事必须服从已校验的需求，而不是重新理解原始字符串。
        requirement = state.get("requirement")
        outline = state.get("story_outline")
        if requirement is None or outline is None:
            raise ValueError("缺少需求或故事大纲，不能生成角色设定")
        return {
            "characters": text_model.generate_characters(requirement, outline),
            "events": ["已生成角色设定"],
        }

    return generate_characters
