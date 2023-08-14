from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_rises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 70
        self.recipe.full_clean()
        self.recipe.save()
        self.fail(self.recipe.title)