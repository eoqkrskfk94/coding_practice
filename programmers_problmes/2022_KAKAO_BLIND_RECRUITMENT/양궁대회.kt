var scoreDiff = -100
var answerCandidate = listOf<Int>()

class Solution {
    fun solution(n: Int, info: IntArray): IntArray {
        var answer = listOf<Int>()

        dfs(0, n,info,MutableList(11) {0})

        if(answerCandidate.isEmpty()) return intArrayOf(-1)


        return answerCandidate.toIntArray()
    }

    fun dfs(position: Int ,n: Int, info: IntArray, result: MutableList<Int>) {

        if(n == 0) {
            var diff = getPointDiffRyanWithApeach(result, info.toList())

            if(diff > 0) {
                if(scoreDiff < diff) {
                    scoreDiff = diff
                    answerCandidate = result.toList()
                } else if(scoreDiff == diff) {
                    answerCandidate = getLeastMarkList(answerCandidate.toList(), result.toList())
                }
            }

            return
        }


        for(i in position .. 10) {

            for (j in 1..n) {
                result[i] += j
                dfs(i, n-j, info, result)
                result[i] -= j
            }
        }

    }

    fun getPointDiffRyanWithApeach(ryanMarks: List<Int> , apeachMarks: List<Int>): Int {
        var ryanScore = 0
        var apeachScore = 0

        for(i in 0 .. 10) {
            if(ryanMarks[i] == 0 && apeachMarks[i] == 0) continue
            if(ryanMarks[i] > apeachMarks[i]) ryanScore += (10 - i)
            else apeachScore += (10 - i)
        }

        return ryanScore - apeachScore
    }

    fun getLeastMarkList(marks1: List<Int>, marks2: List<Int>): List<Int> {

        for(i in 10 downTo 0) {
            if(marks1[i] == 0 && marks2[i] == 0) continue
            if(marks1[i] > marks2[i]) return marks1
            else return marks2
        }

        return marks1
    }
}