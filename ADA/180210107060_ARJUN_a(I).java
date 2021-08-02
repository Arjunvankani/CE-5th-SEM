import java.util.Scanner;

public class insertion
{
	static void insertionsort(int[] arr)
	{
		int n = arr.length;
		for (int i = 1; i < n; i++) {  
            int key = arr[i];  
            int j = i-1;  
            while ( (j > -1) && ( arr [j] > key ) ) {  
                arr [j+1] = arr [j];  
                j--;  
            }  
            arr[j+1] = key;  
        }  
	}
public static void main(String args[]){
	
			Scanner n = new Scanner(System.in);
			int arr[]=new int[10];
			System.out.println("Enter your num...\n");
			for(int i=0;i<arr.length;i++)
			{
				arr[i]= n.nextInt();
			}
		System.out.println("Array Before Insertion sort......\n");
		for(int i=0;i<arr.length;i++)
		{
			System.out.print(arr[i]+" ");
		}
		System.out.println();
		insertionsort(arr);
		System.out.println("Array after Insertion sort......\n");
		for(int i=0;i<arr.length;i++)
		{
		System.out.print(arr[i]+" ");
		}
	}
}