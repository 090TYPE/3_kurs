public sealed class Circle
{   
    private double radius;    
    public Circle(double radius)    
    {      
        this.radius = radius;     
    }
    public double Calculate(Func<double, double> op)
        
    {   
        return op(radius);    
    }   
}    
internal class Program  
{     
    static void Main()    
    {     
        double radius = 3.25;     
        Circle circle = new Circle(radius);  
        Func<double, double> calculateCircumference = r => 3.14 * (2 * r);  
        double circumference = circle.Calculate(calculateCircumference); 
        Console.WriteLine($"Длина окружности с радиусом {radius} равна {circumference}");
    }
}


