import java.util.HashSet;

class Solution {
    String cleanLocalName(String localName) {
        localName.ch
        return localName.replace(".", "").split("\\+")[0];
    }

    public int numUniqueEmails(String[] emails) {
        HashSet<String> uniqueEmails = new HashSet<>();
        for (String email: emails) {
            String emailAddress[] = email.split("@");
            uniqueEmails.add(cleanLocalName(emailAddress[0]) + "@" + emailAddress[1]);
        }
        return uniqueEmails.size();
    }
}
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] emails = new String[]{"test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"};
        int emailCounts = solution.numUniqueEmails(emails);
        System.out.println(emailCounts);
//        System.out.println(solution.cleanLocalName("test.email+alex"));
    }
}
