import unittest

from src.features import build_features
from src.models import train_model, predict_model

class Unit(unittest.TestCase):

    def test_build_features_has_main(self):

        try:
            build_features.main()
        except NotImplementedError:
            fail = True

        if fail:
            self.fail("No main() implemented in build_features.py")

    def test_train_model_has_main(self):

        try:
            train_model.main()
        except NotImplementedError:
            fail = True

        if fail:
            self.fail("No main() implemented in train_model.py")

    def test_predict_model_has_main(self):

        try:
            predict_model.main()
        except NotImplementedError:
            fail = True

        if fail:
            self.fail("No main() implemented in predict_model.py")