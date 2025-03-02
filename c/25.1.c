#include<stdio.h>
int main(){
    int day;
    puts("enter a number between 1to7");
    scanf("%i",&day);
    switch (day)
    {
    case 1:
        puts("mon");
        break;
    case 2:
	puts("tue");
	break;	
	case 3:
		puts("wed");
		break;
		case 4:
			puts("thu");
			break;
			case 5:
			puts("fri");	
				break;
				case 6:
					puts("sat");
					break;
					case 7:
						puts("sun");
						break;
    default:
        puts("no days");
        break;
    }
    return 0;

}