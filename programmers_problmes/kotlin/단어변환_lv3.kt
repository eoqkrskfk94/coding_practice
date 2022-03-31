import kotlin.math.*

class Solution {
    var answer = 0

    fun solution(begin: String, target: String, words: Array<String>): Int {


        dfs(words, MutableList(words.size){false}, begin, target, 0, mutableListOf<String>())

        return answer
    }


    fun dfs(words: Array<String>, visit: MutableList<Boolean>, begin: String, target: String, count: Int, wordList: MutableList<String>) {


        if(begin == target) {
            if(answer == 0) answer = wordList.size
            else answer = min(answer, wordList.size)
        }

        for(i in 0 until words.size) {
            if(visit[i] == false && checkIfStringHasOneCharaterDiff(begin, words[i])) {

                visit[i] = true
                wordList.add(words[i])

                dfs(words, visit, words[i], target, count+1, wordList)

                visit[i] = false
                wordList.removeAt(wordList.lastIndex)
            }
        }

    }

    fun checkIfStringHasOneCharaterDiff(word1: String, word2: String): Boolean {
        var diffCount = 0

        for(i in word1.indices) {
            if(word1[i] != word2[i]) diffCount++
        }

        if(diffCount == 1) return true
        else return false

    }



}