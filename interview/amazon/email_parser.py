"""
Email parser

You are writing an email parser which can extract the "history" part and the "reply" part (everthing but the "history").

Assume that you are given a well parsed DOM tree.

<p>Hi John!</p>
<p>I am fine, thanks!</p>
<blockquote>
<p>Hi Jane, what's up?</p>
</blockquote>

and then you will be given a DOM tree like:




                  [e-mail]
        /              |            \
      /                |              \
<p>                <p>          <blockquote>
/                       |                  \
/                       |                   \
Hi, John!     Thanks!          <p>
                                             |
                                             |
                              Hi Jane, what's up?

please implement 2 APIs:

1. getReply
2. getHistory


givin node def:

class Node {
String tag;
List<Node> children;
List<Attr> attrs;
String text;
}

to simplify the node travelling, only "p" tag has text presented.

follow up:

- some email client is using different way to marking history part, how do you handle?
- what if there are multiple part of "history"?
- how to test it?


"""
class Node:
    def __init__(self, tag, text):
        self.tag = tag
        self.text = text
        self.children = []
        self.attrs = []

    def getReply(self):
        return self.reply


    def getHistory(self):
        return self.history


class EmailParser:
    def __init__(self):
        pass

    def parse(self, message):
        pass

    def run(self, email_message):
        Node = self.parse(email_message)

def main():
    email_message = """<p>Hi John!</p>
<p>I am fine, thanks!</p>
<blockquote>
<p>Hi Jane, what's up?</p>
</blockquote>
    """

    ep = EmailParser()
    ep.run(email_message)

if __name__ == '__main__':
    main()
