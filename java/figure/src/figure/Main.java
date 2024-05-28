package figure;
public class Main {
    public static void main(String[] args) {
        Figure[] shapes = {
            new Triangle("Red", 3, 4, 5),
            new Circle("Blue", 7),
            new Rectangle("Green", 4, 6),
            new Hexagon("Yellow", 2)
        };

        for (Figure shape : shapes) {
            System.out.println("Figure: " + shape.getName());
            System.out.println("Color: " + shape.getColor());
            System.out.println("Perimeter: " + shape.perimeter());
            System.out.println("Area: " + shape.area());
            System.out.println();
        }
    }
}

