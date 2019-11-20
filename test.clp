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
    (assert (rule_used triangle_check))
)

;Checking quadrilateral
(defrule quadrilateral_check
    (count_vertex 4)
    =>
    (assert (shape quadrilateral))
    (assert (rule_used quadrilateral_check))
)

;Checking pentagram
(defrule pentagram_check
    (count_vertex 5)
    =>
    (assert (shape pentagram))
    (assert (rule_used pentagram_check))
)

;Checking hexagram
(defrule hexagram_check
    (count_vertex 6)
    =>
    (assert (shape hexagram))
    (assert (rule_used hexagram_check))
)


;Checking obtuse triangle
(defrule obtuse_triangle_check
    (detected_shape (id ?n) (angle ?a))
    (> ?a 90)
    (shape triangle)
    =>
    (assert (shape obtuse_triangle))
    (assert (rule_used obtuse_triangle_check))
)

;Checking right triangle
(defrule right_triangle_check
    (detected_shape (id ?n) (angle ?a))
    (test(= ?a 90))
    (shape triangle)
    =>
    (assert (shape right_triangle))
    (assert (rule_used right_triangle_check))
)

;Checking acute triangle
(defrule acute_triangle_check
    (detected_shape (id 1) (angle ?a))
    (detected_shape (id 2) (angle ?b))
    (detected_shape (id 3) (angle ?c))
    (test(< ?a 90))
    (test(< ?b 90))
    (test(< ?c 90))
    (shape triangle)
    =>
    (assert (shape acute_triangle))
    (assert (rule_used acute_triangle_check))
)

;Checking equilateral triangle
(defrule equilateral_triangle_check
    (detected_shape (id 1) (length ?n1))
    (detected_shape (id 2) (length ?n2))
    (detected_shape (id 3) (length ?n3))
    (test(< (abs (- ?n1 ?n2)) 6))
    (test(< (abs (- ?n1 ?n2)) 6))
    (test(< (abs (- ?n2 ?n3)) 6))
    (shape triangle)
    =>
    (assert (shape equilateral_triangle))
    (assert (rule_used equilateral_triangle_check))
)

;Checking isosceles triangle
(defrule isosceles_triangle_check
    (detected_shape (id ?n) (length ?x1))
    (detected_shape (id ?m & ~?n) (length ?x2))
    (test(< (abs (- ?x1 ?x2)) 6))
    (shape triangle)
    =>
    (assert (shape isosceles_triangle))
    (assert (rule_used isosceles_triangle_check))
)


; Checking parallelogram
(defrule parallelogram_check
    (detected_shape (id ?n) (length ?x1))
    (detected_shape (id ?m & ~?n) (length ?x2))
    (detected_shape (id ?l & ~?n & ~?m) (length ?y1))
    (detected_shape (id ?k & ~?n & ~?m & ~?l) (length ?y2))
    (test(< (abs (- ?x1 ?x2)) 6))
    (test(< (abs (- ?y1 ?y2)) 6))    
    (shape quadrilateral)
    =>
    (assert (shape parallelogram))
    (assert (rule_used parallelogram_check))
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
    (assert (rule_used rectangle_check))
)

; Checking kite
(defrule kite
    (detected_shape (id ?n) (angle ~90))
    (shape parallelogram)
    =>
    (assert (shape kite)) 
    (assert (rule_used kite))
)

; Checking trapezoid
(defrule trapezoid_check
    (detected_shape (id ?n) (angle ?a))
    (detected_shape (id ?m & ~?n) (angle ?b))
    (detected_shape (id ?l & ~?n & ~?m) (angle ?c))
    (detected_shape (id ?k & ~?l & ~?m & ~?n) (angle ?d))
    (detected_shape (id ?j) (length ?x))
    (detected_shape (id ?i & ~?j) (length ?y))
    (test(> (abs (- ?x ?y)) 6))
    (detected_shape (id ?h & ~?i & ~?j) (length ?z))
    (test(> (abs (- ?z ?x)) 6))
    (test(> (abs (- ?z ?y)) 6))
    (test (= (+ ?a ?c) 180))
    (test (= (+ ?b ?d) 180)) 
    (shape quadrilateral)
    =>
    (assert (shape trapezoid))
    (assert (rule_used trapezoid_check))
)

; Checking isosceles trapezoid
(defrule isosceles_trapezoid
    (detected_shape (id ?n) (length ?x1))
    (detected_shape (id ?m & ~?n) (length ?x2))
    (test(< (abs (- ?x1 ?x2)) 6))
    (shape trapezoid)
    =>
    (assert (shape isosceles_trapezoid))
    (assert (rule_used isosceles_trapezoid))
)

; Checking left trapezoid
(defrule left_trapezoid_check
    (detected_shape (id 1) (angle 90))
    (detected_shape (id 2) (angle 90))
    (shape trapezoid)
    =>
    (assert (shape left_trapezoid))
    (assert (rule_used left_trapezoid_check))
)

; Checking right trapezoid
(defrule right_trapezoid_check
    (detected_shape (id 3) (angle 90))
    (detected_shape (id 4) (angle 90))
    (shape trapezoid)
    =>
    (assert (shape right_trapezoid))
    (assert (rule_used right_trapezoid_check))
)

; Checking equilateral pentagram
(defrule equilateral_pentagram_check
    (detected_shape (id 1) (length ?x1))
    (detected_shape (id 2) (length ?x2))
    (detected_shape (id 3) (length ?x3))
    (detected_shape (id 4) (length ?x4))
    (detected_shape (id 5) (length ?x5))
    (test(< (abs (- ?x1 ?x2)) 6))
    (test(< (abs (- ?x1 ?x3)) 6))
    (test(< (abs (- ?x1 ?x4)) 6))
    (test(< (abs (- ?x1 ?x5)) 6))
    (test(< (abs (- ?x2 ?x3)) 6))
    (test(< (abs (- ?x2 ?x4)) 6))
    (test(< (abs (- ?x2 ?x5)) 6))
    (test(< (abs (- ?x3 ?x4)) 6))
    (test(< (abs (- ?x3 ?x5)) 6))
    (test(< (abs (- ?x4 ?x5)) 6))
    (shape pentagram)
    =>
    (assert (shape equilateral_pentagram))
    (assert (rule_used equilateral_pentagram_check))
)

; Checking equilateral hexagram
(defrule equilateral_hexagram_check
    (detected_shape (id 1) (length ?x1))
    (detected_shape (id 2) (length ?x2))
    (detected_shape (id 3) (length ?x3))
    (detected_shape (id 4) (length ?x4))
    (detected_shape (id 5) (length ?x5))
    (detected_shape (id 6) (length ?x6))
    (test(< (abs (- ?x1 ?x2)) 6))
    (test(< (abs (- ?x1 ?x3)) 6))
    (test(< (abs (- ?x1 ?x4)) 6))
    (test(< (abs (- ?x1 ?x5)) 6))
    (test(< (abs (- ?x1 ?x6)) 6))
    (test(< (abs (- ?x2 ?x3)) 6))
    (test(< (abs (- ?x2 ?x4)) 6))
    (test(< (abs (- ?x2 ?x5)) 6))
    (test(< (abs (- ?x2 ?x6)) 6))
    (test(< (abs (- ?x3 ?x4)) 6))
    (test(< (abs (- ?x3 ?x5)) 6))
    (test(< (abs (- ?x3 ?x6)) 6))
    (test(< (abs (- ?x4 ?x5)) 6))
    (test(< (abs (- ?x4 ?x6)) 6))
    (test(< (abs (- ?x5 ?x6)) 6))
    =>
    (assert (shape equillateral_hexagram))
    (assert (rule_used equilateral_hexagram_check))
)
