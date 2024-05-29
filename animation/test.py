from manim import *
import json

with open("output.json") as f:
    data = json.load(f)
    
found_objects, found_objects_keypoints, template_points_matched, splitted_template, template_points = data.values()
    
class ImageRectanglesAnimation(Scene):
    def drawPoints(self, image, points):
        # Draw all the points defind in the list
        # The point is defined as a tuple
        # (x, y) defining the pixel position of the point
        # The coordinates are relative to the image
        # Top left corner of the image is (0, 0)
        # Bottom right corner of the image is (width, height)

        animations = []
        for point in points:
            x, y = point
            dot = Dot(color=RED).scale(0.5)
            
            # q: how many unit step is the image width and height?
            # a: 1
            
            dot.move_to(image.get_corner(UL) + RIGHT * image.width * x + DOWN * image.height * y)
            # Add the creation of the dot to the list of animations
            animations.append(Create(dot))        
        # Play all the animations
        self.play(*animations)
        
    def drawRectangles(self, image, rects):
        # Draw all the rects defind in the list
        # The rect is defined as a tuples
        # (x, y, width, height)
        # The coordinates are relative to the image
        # Top left corner of the image is (0, 0)
        # Bottom right corner of the image is (1, 1)
        animations = []
        for rect in rects:
            width, height, x, y = rect
            rect = Rectangle(width=image.width * width, height=image.height * height, fill_opacity=.5)
            # Add the creation of the rectangle to the list of animations
            animations.append(Create(rect.move_to(image.get_corner(UL) + RIGHT * image.width * x + DOWN * image.height * y)))
        
        # Play all the animations
        self.play(*animations)    
            
    def construct(self):
        # Load images
        image1 = ImageMobject("anim1.png")
        image2 = ImageMobject("anim2.png")
        
        # Resize images
        #image1.scale(2)
        #image2.scale(2)
        image2.set_height(image1.get_height())
        
        # Position images
        image1.to_edge(LEFT)
        image2.to_edge(RIGHT)

        # Add images to the scene
        self.add(image1, image2)

        # Create three rectangles on the first image
        """
        rect1 = Rectangle(width=image1.width, height=image1.height / 3, fill_opacity=.5).move_to(image1.get_top() + DOWN * image1.height / 6).set_fill(PURPLE)
        rect2 = Rectangle(width=image1.width, height=image1.height / 3, fill_opacity=.5).move_to(image1.get_center()).set_fill(PURPLE)
        rect3 = Rectangle(width=image1.width, height=image1.height / 3, fill_opacity=.5).move_to(image1.get_bottom() + UP * image1.height / 6).set_fill(PURPLE)
        
        # Add rectangles to the scene
        self.play(Create(rect1), Create(rect2), Create(rect3))
        
        # Change the width of the rectangles to be 1/3 of the image2
        self.play(
            rect1.animate.move_to(image2.get_top() + DOWN * image2.height / 6 + LEFT * image2.width / 3).set_width(image2.width / 3).set_fill(ORANGE),
            rect2.animate.move_to(image2.get_center()).set_width(image2.width / 3).set_fill(BLUE),
            rect3.animate.move_to(image2.get_bottom() + UP * image2.height / 6 + RIGHT * image2.width / 3).set_width(image2.width / 3).set_fill(GREEN),
            run_time=2
        )

        # Keep the animation on screen for a while before ending
        self.wait(2)
        
        self.play(
            rect2.animate.move_to(image2.get_center() + LEFT * image2.width / 3).set_fill(ORANGE),
            rect3.animate.move_to(image2.get_bottom() + UP * image2.height / 6 + LEFT * image2.width / 3).set_fill(ORANGE),
        )
        
        """
        
        # self.drawPoints(image1, [(0.5, 0.5), (0.25, 0.75), (0.75, 0.25)])
        self.drawPoints(image1, template_points)
        
        self.drawRectangles(image1, splitted_template)
        
        self.wait(2)

# To render the scene, use the command:
# manim -pql script_name.py ImageRectanglesAnimation
