function findFactorial(number)
{
    let fact=1;
    for(let i=1; i<=number; i++)
    {
        fact=fact*i;
    }
    return fact;
}
console.log(findFactorial(5));
console.log(findFactorial(6));