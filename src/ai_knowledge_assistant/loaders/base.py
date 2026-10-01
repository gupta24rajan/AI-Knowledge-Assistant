from abc import ABC, abstractmethod
"""
ABC → abstract class banane ke liye
abstractmethod → method ka rule define karne ke liye
"""

class DocumentLoader(ABC):    #  1>.Ye khud actual PDF read nahi karega.  2>.Ye basically rule/contract define karega.

    @abstractmethod #Jo bhi class DocumentLoader ko inherit karegi, usko load() method provide karna padega.
    def load(self):
        pass



"""
🧠 Mental Model

Isko aise imagine karo:

              DocumentLoader
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
      PDFLoader           TextLoader
          │                   │
       load()               load()
          │                   │
       PDF read            TXT read

Base class bolti hai:

"Tum loader ho? Toh tumhare paas load() method hona chahiye."

Lekin kaise load karna hai, ye child class decide karegi.

"""