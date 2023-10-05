Console.Write("Введите число: ");
string userInput = Console.ReadLine();

if (int.TryParse(userInput, out int number))
{
    if (userInput.Length >= 4)
    {
        int fourthFromRight = int.Parse(userInput.Substring(userInput.Length - 4, 1));

        if (fourthFromRight == 1)
        {
            Console.WriteLine("В данном числе 1 тысяча.");
        }
        else
        {
            Console.WriteLine($"В данном числе {fourthFromRight} тысячи.");
        }
    }
    else
    {
        Console.WriteLine("Число должно состоять как минимум из 4 цифр.");
    }
}
else
{
    Console.WriteLine("Введено некорректное число.");
}