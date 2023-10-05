class Program
{
    static void Main()
    {
        Console.Write("Введите число: ");
        if (int.TryParse(Console.ReadLine(), out int number))
        {
            bool satisfiesCriteria = (number % 4 == 0) && (number >= 10);

            if (satisfiesCriteria)
            {
                Console.WriteLine("Число удовлетворяет обоим критериям.");
            }
            else
            {
                Console.WriteLine("Число не удовлетворяет обоим критериям.");
            }
        }
        else
        {
            Console.WriteLine("Введено некорректное число.");
        }
    }
}