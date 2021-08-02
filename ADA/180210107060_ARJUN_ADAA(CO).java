import java.util.Scanner;

public class couting
{
	static void coutingsort(int[] arr)
	{
	int n = arr.length;
	int temp[] = new int[50];
	
	int count[] = new int[50];
	  
	for(int i = 0; i<10; ++i)
		count[i] = 0;
	
	for(int i=0; i<n; ++i)
		++count[arr[i]];
	
	for(int i=1; i<50; ++i)
		count[i] += count[i-1];
	
	for(int i = n-1; i>=0; i--)
	{
		temp[count[arr[i]]-1] = arr[i];
		--count[arr[i]];
	}
	
	for(int i=0; i<n; ++i)
		arr[i] = temp[i];
	
	}
public static void main(String args[]){
	
			Scanner n = new Scanner(System.in);
			int arr[]=new int[10];
			System.out.println("Enter your num...\n");
			for(int i=0;i<arr.length;i++)
			{
				arr[i]= n.nextInt();
			}
			System.out.println("Array Before Couting  sort......\n");
			for(int i=0;i<arr.length;i++)
			{
				System.out.print(arr[i]+" ");
			}
			System.out.println();
			coutingsort(arr);
			System.out.println("Array after Couting sort......\n");
			for(int i=0;i<arr.length;i++)
			{
			System.out.print(arr[i]+" ");
			}
	}
}