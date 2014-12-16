# Complexity in software development

## Jonas Juselius <jonas.juselius@uit.no>

HPC@UiT

---

layout: false

## The tar pit

* Over time software tends to become harder and harder to reason about
* The code bse easily becomes untidy ("I'll fix it later")
* Small changes become harder to implement
* Hacks and workarounds trump design
* Bugs start appearing where in unexpected places
* More time is spent debugging than developing
* Complexity strangles development

---

## Causes of complexity

* Our tools and languages
* Poor design or wrong design
* Not enough resources (e.g. time)

<img src="{{base}}/img/joe-paradiso-modular-synth-front.png" style="width: 70%;"/>

---

## The dark side

<img src="{{base}}/img/joe-paradiso-modular-synth-back.png" style="width: 70%;"/>

---

## The brain facing computer code

<img src="{{base}}/img/Homer-simpson-brain.jpg" style="width: 100%;"/>

---

## Inherent vs. incidental complexity

We distinguish between two types of complexity:

* *Inherent* complexity of the problems space
* *Incidental* complexity in the solution space
* Complexity implies braiding and intertwining
* Simplicity implies "one foldedness", i.e. one braid, single entity

<img src="{{base}}/img/tincan.png" style="width: 55%;"/>

---

## Stockholm telephone tower anno 1910

<img src="{{base}}/img/stockholm-tower.jpg" style="width: 75%;"/>

---

## Simple vs. easy

* Simple is not the same as easy
* Simple means:
    * One role or tasks
    * One concept or dimension
* Easy means:
    * Familiarity
    * Near at hand
* Just because you know it does not make it simple

---

## Development speed


<img src="{{base}}/img/develspeed.jpg" style="width: 75%;"/>

---

## Simplicity

* Simplicity is the prerequisite of reliability (E. Dijkstra)
* We can only consider a very limited number of things at once
* Complex things must be considered together, undermining understanding
* We can only hope to make reliable things we understand

<img src="{{base}}/img/Lady-Juggler.png" style="width: 40%;"/>

---

## Benefits of simplicity

* Easy to understand
* Easy to change
* Easy to debug
* Simplicity is much harder than complexity!

_"Simplicity is the ultimate sophistication. L. da Vinci."_

---

## Enemy of the state

* The no. 1 cause of complexity is *state*, i.e. variables
* Every mutable variable is stateful
* For every bit of state in your program, there are two tests: A program with
  100 integer variables has $2^{3200}$ distinct states.

<img src="{{base}}/img/alfred_e_neuman_1.jpg" style="width: 30%;"/>

---

## Local variables are stateful too

$f(x) = (n+1)(n+2)$

```{Python}
    def f(x):
        x = x + 1
        y = x + 1
        return x * y
```

$f(x) = (n+1)^2$

```{Python}
    def f(x):
        y = x + 1
        x = x + 1
        return x * y
```

---

## Referential transparency

```{Python}
    def f(x):
        x1 = x + 1
        y1 = x1 + 1
        return x1 * y1
```

Haskell example:

```{Haskell}
    f :: (Num a) => a -> a
    f x = x' * y'
        where
            y' = x' + 1
            x' = x + 1
```

---

## Me, preparing to mutate some state

<img src="{{base}}/img/heavy_diver1.jpg" style="width: 50%;"/>

---

## State of affairs

* Information vs. place
* PLOP: New information replaces old
* Facts don't change because we ignore them
* PLOP grew out of tiny computer memories
* Information is simple, don't ruin it
* We use values on the wire, why not in our codes?

---


## The value of values

* Values are immutable
* Values can be shared
* Values are easy to fabricate
* Values are language agnostic
* Values aggregate. Objects don't (usually)
* Values are stable: reproducible results
* Values don't *need* methods
* Values have representation, *not* implementation

---

## Concurrency

* Concurrency in imperative code is very hard
* You are totally lost in the dark without a good thread checker
* In a pure, immutable world concurrency is nearly trivial!

<img src="{{base}}/img/floor-loom-diagram.jpg" style="width: 55%;"/>

---

## Composition

* Composition enables us to build complex behavior from simple components
* We can reason about the components, and we can reason about the composite
* Composition is key to managing complexity
* Modularity does not imply simplicity, but is enabled by it

<img src="{{base}}/img/knit_vs_lego.jpg" style="width: 100%;"/>

---

## The proof of the pudding

* Can you move sub-systems?
    * To another language?
    * To another machine?
    * Without changing much?

<img src="{{base}}/img/under_the_hood.png" style="width: 50%;"/>

---

## How about object-oriented programming?

* Encapsulation: Adding implementation to information?
* Complects both state and information
* OOP lures us to implement with little, moving machines


> The problem with object-oriented languages is they've got all this implicit
> environment that they carry around with them. You wanted a banana but what you
> got was a gorilla holding the banana and the entire jungle.
>
> Joe Armstrong

---

## A base class

```{Python}
    class A(object):
        def __init__(self):
            self.a = 1

        def addone(self, x):
            self.a += 1
            return x + self.a

        def inc(self, x):
            return x + self.a
```

---

## Hidden state, crouching dragon

```{Python}
    class B(A):
        def __init__(self):
            super(B,self).__init__()

        def np1np2(self, x):
            a = self.addone(x)
            b = self.inc(x)
            return a * b

    b = B()
    print b.np1np2(5)
```

---

## It all started really simple

<img src="{{base}}/img/complex-machine.jpg" style="width: 55%;"/>

---

## Code quality

Every bug has passed both the type checker and the test suite.

<img src="{{base}}/img/wtfs_per_minute_thumb.jpg" style="width: 45%;"/>

