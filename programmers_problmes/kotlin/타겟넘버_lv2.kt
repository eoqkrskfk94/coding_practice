class Solution {
    var answer = 0
    var targetCount = 0

    fun solution(numbers: IntArray, target: Int): Int {

        targetCount = target

        dfs(numbers, 0, 0, numbers.size)

        return answer
    }


    fun dfs(numbers: IntArray, count : Int, comb: Int, length: Int) {

        if(count == length) {
            if(targetCount == comb) answer++
            return
        }

        dfs(numbers, count+1, comb + numbers[count], length)
        dfs(numbers, count+1, comb - numbers[count], length)
    }
}