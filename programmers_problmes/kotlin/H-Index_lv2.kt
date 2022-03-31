class Solution {
    fun solution(citations: IntArray): Int {
        var answer = citations.size

        val list = citations.sorted()

        list.forEachIndexed { index, citation ->
            if(answer <= citation) {
                return answer
            }
            answer--
        }

        return answer
    }
}