class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        List<Integer> [] buckets = new List[nums.length+1];
        for(int n: nums){
            counter.put(n, counter.getOrDefault(n, 0)+1);
        }

        for (int i = 0; i < buckets.length; i++){
            buckets[i] = new ArrayList<>();
        }

        for (Map.Entry<Integer, Integer> entry: counter.entrySet()){
            buckets[entry.getValue()].add(entry.getKey());
        }

        int [] result = new int[k];
        int index = 0;
        for (int freq = buckets.length-1; freq > 0; freq--){
            for (int num: buckets[freq]){
                result[index++] = num;
                if (index == k){
                    return result;
                }
            }
        }
        return result;
    }
}
