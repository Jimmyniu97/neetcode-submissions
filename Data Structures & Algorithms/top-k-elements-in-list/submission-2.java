class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for(int num: nums){
            count.put(num, count.getOrDefault(num, 0)+1);
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)-> Integer.compare(a[1], b[1]));
        for(Map.Entry<Integer, Integer> entry: count.entrySet()){
            pq.offer(new int[]{entry.getKey(), entry.getValue()});
            if (pq.size() > k) {
            pq.poll();
            }
        }
        int[] result = new int[k];
        int i = 0;
        while (!pq.isEmpty()){
            result[i++] = pq.poll()[0];
        }
        return result;
    }
}
