from django.forms import ValidationError

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_the_test(self):
        self.recipe.title = 'A' * 70

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
