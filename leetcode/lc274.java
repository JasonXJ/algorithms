/* See lc274.py for an O(n) solution */
public class Solution {
	public int hIndex(int[] citations) {
		Arrays.sort(citations);
		int i = citations.length - 1;
		for (; i >= 0; --i) {
			if (citations.length - i > citations[i])
				break;
		}
		i += 1;
		if (i < citations.length)
			return citations.length - i;
		return 0;
	}

}
