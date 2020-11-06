import unittest

class Test_robot(unittest.TestCase):
    def test_right_back(self):
        with captured_io(StringIO('HAL\nright\nback 10\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (-10,0).
HAL: What must I do next? HAL: Shutting down..""", output[-212:])
        pass