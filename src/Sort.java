

import java.util.Random;

public class Sort {

	private Sort(){

	}

	public static <T extends Comparable<T>> T[] Bogosort(T[] list){
		//Check if list is sorted
		if(isSorted(list) == true){
			return list;
		}
		else{
			//Bogo?
			shuffleArray(list);
			//Bogo.
			return Bogosort(list);
		}
	}

	//Fisher-Yates(?) shuffle
	public static <T extends Comparable<T>> void shuffleArray(T[] ar) 
	{
		Random rnd = new Random();
		for (int i = ar.length - 1; i > 0; i--)
		{
			int index = rnd.nextInt(i + 1);
			// Simple swap
			T a = ar[index];
			ar[index] = ar[i];
			ar[i] = a;
		}
	}

	//Generic isSorted()
	public static <T extends Comparable<T>> Boolean isSorted(T[] list){
		T prev = null;
		for( T elem : list ) {
			if( prev != null && prev.compareTo(elem) > 0 ) {
				return false;
			}
			prev = elem;
		}
		return true;
	}

}
