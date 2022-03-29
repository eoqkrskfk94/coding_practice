class Solution {
    fun solution(numbers: IntArray): String {
        var answer = ""
        var listOfNumbers = mutableListOf<List<Int>>()

        numbers.forEach {
            val number = it.toString()
            when(it.toString().length) {
                1 -> {
                    listOfNumbers.add(listOf(it, number.repeat(4).toInt()))
                }
                2 -> {
                    listOfNumbers.add(listOf(it, number.repeat(2).toInt()))
                }
                3 -> {
                    listOfNumbers.add(listOf(it, number.repeat(2).substring(0,4).toInt()))
                }
                4 -> {
                    listOfNumbers.add(listOf(it, number.toInt()))
                }
            }
        }

        answer = listOfNumbers.sortedByDescending {it[1]}.map {it[0]}.joinToString("")

        if(answer.toDouble() == 0.0) {
            return "0"
        }

        return answer
    }
}