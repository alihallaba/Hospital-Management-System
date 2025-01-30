
package src.hms;

import java.util.List;

public class Forum {
    private List<Question> questions;

    public void addQuestion(Question question) {
        questions.add(question); // Add question to list
    }

    public void removeQuestion(Question question) {
        questions.remove(question); // Remove question from list
    }
}
