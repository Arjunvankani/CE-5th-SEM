import java.util.Scanner;

public class BinarySearch { 
    int binarySearch(int arr[], int l, int h, int key) 
    { 
        if (h >= l) { 
            int mid = l + (h - l) / 2; 
  
            
            if (arr[mid] == key) 
                return mid; 
            
            if (arr[mid] > key) 
                return binarySearch(arr, l, mid - 1, key); 
  
            return binarySearch(arr, mid + 1, h, key); 
        } 
  
       
        return -1; 
    } 
  

    public static void main(String args[]) 
    { 
      
        Scanner n = new Scanner(System.in);
		int arr[]=new int[10];
		System.out.println("Enter your num...\n");
		for(int i=0;i<arr.length;i++)
			{
				arr[i]= n.nextInt();
			}
			
		Scanner n1 = new Scanner(System.in);
		System.out.print("Search the element ..\t");
		int key = n1.nextInt();
		
		BinarySearch bs = new BinarySearch();
			
        int result = bs.binarySearch(arr, 0,arr.length - 1, key); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 