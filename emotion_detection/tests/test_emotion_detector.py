import unittest
from emotion_detection.emotion_detection import emotion_detector # Assuming emotion_detector.py is directly in emotion_detection/

class TestEmotionDetector(unittest.TestCase):
    """
    Unit tests for the emotion_detector function.
    """

    def test_joy_emotion(self):
        """
        Tests if 'joy' is the dominant emotion for a happy statement.
        """
        text = "I am glad this happened"
        result = emotion_detector(text)
        self.assertIsNotNone(result, f"API call failed for text: '{text}'")
        self.assertIn('dominant_emotion', result, f"Dominant emotion not found in result for text: '{text}'")
        self.assertEqual(result['dominant_emotion'], 'joy',
                         f"Expected 'joy' but got '{result.get('dominant_emotion')}' for text: '{text}'")

    def test_anger_emotion(self):
        """
        Tests if 'anger' is the dominant emotion for an angry statement.
        """
        text = "I am really mad about this"
        result = emotion_detector(text)
        self.assertIsNotNone(result, f"API call failed for text: '{text}'")
        self.assertIn('dominant_emotion', result, f"Dominant emotion not found in result for text: '{text}'")
        self.assertEqual(result['dominant_emotion'], 'anger',
                         f"Expected 'anger' but got '{result.get('dominant_emotion')}' for text: '{text}'")

    def test_disgust_emotion(self):
        """
        Tests if 'disgust' is the dominant emotion for a disgusted statement.
        """
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertIsNotNone(result, f"API call failed for text: '{text}'")
        self.assertIn('dominant_emotion', result, f"Dominant emotion not found in result for text: '{text}'")
        self.assertEqual(result['dominant_emotion'], 'disgust',
                         f"Expected 'disgust' but got '{result.get('dominant_emotion')}' for text: '{text}'")

    def test_sadness_emotion(self):
        """
        Tests if 'sadness' is the dominant emotion for a sad statement.
        """
        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertIsNotNone(result, f"API call failed for text: '{text}'")
        self.assertIn('dominant_emotion', result, f"Dominant emotion not found in result for text: '{text}'")
        self.assertEqual(result['dominant_emotion'], 'sadness',
                         f"Expected 'sadness' but got '{result.get('dominant_emotion')}' for text: '{text}'")

    def test_fear_emotion(self):
        """
        Tests if 'fear' is the dominant emotion for a fearful statement.
        """
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertIsNotNone(result, f"API call failed for text: '{text}'")
        self.assertIn('dominant_emotion', result, f"Dominant emotion not found in result for text: '{text}'")
        self.assertEqual(result['dominant_emotion'], 'fear',
                         f"Expected 'fear' but got '{result.get('dominant_emotion')}' for text: '{text}'")


if __name__ == '__main__':
    unittest.main()