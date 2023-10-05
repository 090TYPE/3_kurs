int a;

do
{
    Console.WriteLine("Введите целое число:");
}

while (!int.TryParse(Console.ReadLine(), out a));

for (int i = 1; i <= a; i++)
{
    Console.Write(i + " ");
}

for (int i = a - 1; i >= 1; i--)
{
    Console.Write(i + " ");
}

Console.WriteLine();