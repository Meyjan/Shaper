(deftemplate detected_shape
    (slot id)
    (slot angle)
    (slot length)
)

;Checking triangle
(defrule triangle_check
    (count_vertex 3)
    =>
    (assert (shape triangle))
)

;Checking quadrilateral
(defrule quadrilateral_check
    (count_vertex 4)
    =>
    (assert (shape quadrilateral))
)

;Checking pentagram
(defrule pentagram_check
    (count_vertex 5)
    =>
    (assert (shape pentagram))
)

;Checking hexagram
(defrule hexagram_check
    (count_vertex 6)
    =>
    (assert (shape hexagram))
)


;Checking obtuse triangle
(defrule obtuse_triangle_check
    (detected_shape (id ?n) (angle ?a))
    (> ?a 90)
    (shape triangle)
    =>
    (assert (shape obtuse_triangle))
)

;Checking right triangle
(defrule right_triangle_check
    (detected_shape (id ?n) (angle ?a))
    (test(= ?a 90))
    (shape triangle)
    =>
    (assert (shape right_triangle))
)

;Checking acute triangle
(defrule acute_triangle_check
    (detected_shape (id 1) (angle ?a))
    (detected_shape (id 2) (angle ?b))
    (detected_shape (id 3) (angle ?c))
    (< ?a 90)
    (< ?b 90)
    (< ?c 90)
    (shape triangle)
    =>
    (assert (shape acute_triangle))
)

;Checking equilateral triangle
(defrule equilateral_triangle_check
    (detected_shape (id 1) (length ?n))
    (detected_shape (id 2) (length ?n))
    (detected_shape (id 3) (length ?n))
    (shape triangle)
    =>
    (assert (shape equilateral_triangle))
)

;Checking isosceles triangle
(defrule isosceles_triangle_check
    (detected_shape (id ?n) (length ?x))
    (detected_shape (id ?m & ~?n) (length ?x))
    (shape triangle)
    =>
    (assert (shape isosceles_triangle))
)


; Checking parallelogram
(defrule parallelogram_check
    (detected_shape (id ?n) (length ?x))
    (detected_shape (id ?m & ~?n) (length ?x))
    (detected_shape (id ?l & ~?n & ~?m) (length ?y))
    (detected_shape (id ?k & ~?n & ~?m & ~?l) (length ?y))
    (shape quadrilateral)
    =>
    (assert (shape parallelogram))
)

; Checking rectangle
(defrule rectangle_check
    (detected_shape (id ?n) (angle 90))
    (detected_shape (id ?m & ~?n) (angle 90))
    (detected_shape (id ?l & ~?n & ~?m) (angle 90))
    (detected_shape (id ?k & ~?n & ~?m & ~?l) (angle 90))
    (shape parallelogram)
    =>
    (assert (shape rectangle))
)

; Checking kite
(defrule kite
    (detected_shape (id ?n) (angle ~90))
    (shape parallelogram)
    =>
    (assert (shape kite)) 
)

; Checking trapezoid
(defrule trapezoid_check
    (detected_shape (id ?n) (angle ?a))
    (detected_shape (id ?m & ~?n) (angle ?b))
    (detected_shape (id ?l & ~?n & ~?m) (angle ?c))
    (detected_shape (id ?k & ~?l & ~?m & ~?n) (angle ?d))
    (detected_shape (id ?j) (length ?x))
    (detected_shape (id ?i & ~?j) (length ?y & ~?x))
    (detected_shape (id ?h & ~?i & ~?j) (length ~?y & ~?x))
    (test (= (+ ?a ?c) 180))
    (test (= (+ ?b ?d) 180)) 
    (shape quadrilateral)
    =>
    (assert (shape trapezoid))
)

; Checking isosceles trapezoid
(defrule isosceles_trapezoid
    (detected_shape (id ?n) (length ?x))
    (detected_shape (id ?m & ~?n) (length ?x))
    (shape trapezoid)
    =>
    (assert (shape isosceles_trapezoid))
)

; Checking left trapezoid
(defrule left_trapezoid_check
    (detected_shape (id 1) (angle 90))
    (detected_shape (id 2) (angle 90))
    (shape trapezoid)
    =>
    (assert (shape left_trapezoid))
)

; Checking right trapezoid
(defrule right_trapezoid_check
    (detected_shape (id 3) (angle 90))
    (detected_shape (id 4) (angle 90))
    (shape trapezoid)
    =>
    (assert (shape right_trapezoid))
)

; Checking equilateral pentagram
(defrule equilateral_pentagram_check
    (detected_shape (id 1) (length ?x))
    (detected_shape (id 2) (length ?x))
    (detected_shape (id 3) (length ?x))
    (detected_shape (id 4) (length ?x))
    (detected_shape (id 5) (length ?x))
    (shape pentagram)
    =>
    (assert (shape equilateral_pentagram))
)

; Checking equilateral heax
(defrule equilateral_pentagram_check
    (detected_shape (id 1) (length ?x))
    (detected_shape (id 2) (length ?x))
    (detected_shape (id 3) (length ?x))
    (detected_shape (id 4) (length ?x))
    (detected_shape (id 5) (length ?x))
    (detected_shape (id 6) (length ?x))
    =>
    (assert (shape equillateral_hexagram))
)
