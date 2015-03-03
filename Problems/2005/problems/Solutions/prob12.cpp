// prob12.cpp
// HP Codewars 2005
// Arithmetic Expressions
//

//---------------------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#pragma hdrstop
//---------------------------------------------------------------------------
const int MAX_STACK_SIZE = 32;
//---------------------------------------------------------------------------
template< class T >
class Stack
{
  private:
    T stackArray[ MAX_STACK_SIZE ];
    int stackIndex;

  public:
    Stack( void ) : stackIndex(0) { };
    void Reset( void ) { stackIndex = 0; };
    int  Size( void )  { return stackIndex; };
    void Push( T item ) // add item to top
    { // error checking, but no error handling
      if( stackIndex < MAX_STACK_SIZE )
        stackArray[ stackIndex++ ] = item;
    }
    T Pop( void ) // remove top item
    { // error checking, but no error handling
      T result = (T) 0;
      if( stackIndex > 0 )
        result = stackArray[ --stackIndex ];
      return result;
    }
    T Peek( void ) // look at top item without removing it
    { // no error checking
      return stackArray[ stackIndex-1 ];
    }
};
//---------------------------------------------------------------------------
Stack<char>    OperatorStack;
Stack<double>  ValueStack;
//---------------------------------------------------------------------------
#define tokenValue(t)     atof(t)
#define tokenOperator(t)  t[0]
//---------------------------------------------------------------------------
bool IsOperator( char c )
{
  bool result = false;
  if( c == '+' || c == '-' || c == '(' || c == ')' ||
      c == '*' || c == '/' || c == '^' || c == '!' )
  {
    result = true;
  }
  return result;
}
//---------------------------------------------------------------------------
int Precedence( char op )
{
  if(      op == '(' || op == ')' )
    return 5;
  else if( op == '!' )
    return 4;
  else if( op == '^' )
    return 3;
  else if( op == '*' || op == '/' )
    return 2;
  else if( op == '+' || op == '-' )
    return 1;
  else
    return 0;
}
//---------------------------------------------------------------------------
int lineIndex;
char line[81];
bool ReadLine( void )
{
  fprintf( stdout, "expr: " );
  fscanf( stdin, "%[^\n]%*c", line );
  lineIndex = 0;
  return( line[0] == '*' ? false : true );
}
//---------------------------------------------------------------------------
char* GetNextToken( void )
{
  static char token[81];
  int tokenIndex = 0;
  int lineLength = strlen( line );
  // skip white space
  while( lineIndex < lineLength && line[ lineIndex ] <= 32 )
    ++lineIndex;

  if( IsOperator( line[ lineIndex ] ) ) // operator
    token[ tokenIndex++ ] = line[ lineIndex++ ];
  else // real number, terminated by white space or operator
  {
    while( lineIndex < lineLength &&
           line[ lineIndex ] > 32 &&
           ! IsOperator( line[ lineIndex ] ) )
      token[ tokenIndex++ ] = line[ lineIndex++ ];
  }
  // terminate token string
  token[ tokenIndex ] = 0;
  return token;
}
//---------------------------------------------------------------------------
double Operate( double value1, char stackOp, double value2 )
{
  switch( stackOp )
  {
    case '+' : return value1 + value2;
    case '-' : return value1 - value2;
    case '*' : return value1 * value2;
    case '/' : return value1 / value2;
    case '^' : return pow( value1, value2 );
    // no factorial here; it's a unary operator
    default: return 0.0; // this should never happen, right?
  }
}
//---------------------------------------------------------------------------
double Factorial( double n )
{
  double result = n;
  while( n > 1.0 )
  {
    n -= 1.0;
    result *= n;
  }
  return result;
}
//---------------------------------------------------------------------------
void EvalStack( void )
{
  while( ValueStack.Size() > 1  )
  {
    char op = OperatorStack.Pop();

    if( op == '(' )
      break; // stop eval on closed paren

    double value2 = ValueStack.Pop();
    double value1 = ValueStack.Pop();

    ValueStack.Push( Operate( value1, op, value2 ) );
  }
}
//---------------------------------------------------------------------------
#pragma argsused
int main(int argc, char* argv[])
{
  while( ReadLine() )
  {
    bool    prevTokenOperator = false;
    double  valueSign = 1.0;
    char*   token = GetNextToken();
    while( strlen( token ) )
    {
      char op = tokenOperator(token);
      if( IsOperator( op ) )
      {
        valueSign = 1.0;
        // check for negative sign
        if( prevTokenOperator && op == '-' )
          valueSign = -1.0;
        else if( op == ')' )
          EvalStack();
        else if( token[0] == '!' )
          ValueStack.Push( Factorial( ValueStack.Pop() ) );
        else
        {
          char stackOp = OperatorStack.Peek();
          while( OperatorStack.Size() > 0 && stackOp != '(' &&
                 Precedence( op ) <= Precedence( stackOp ) )
          {
            OperatorStack.Pop();
            double value2 = ValueStack.Pop();
            double value1 = ValueStack.Pop();
            ValueStack.Push( Operate( value1, stackOp, value2 ) );
            stackOp = OperatorStack.Peek();
          }
          OperatorStack.Push( op );
          prevTokenOperator = true;
        }
      }
      else
      {
        ValueStack.Push( tokenValue( token ) * valueSign );
        prevTokenOperator = false;
      }
      token = GetNextToken();
    }
    EvalStack();
    printf( "%lf\n", ValueStack.Pop() );
    OperatorStack.Reset();
    ValueStack.Reset();
  }

  return 0;
}
//---------------------------------------------------------------------------
