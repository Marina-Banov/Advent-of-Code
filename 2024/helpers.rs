use std::ops;

#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
pub(crate) struct Point<T> {
    pub(crate) i: T,
    pub(crate) j: T,
}

impl<T> Point<T> {
    pub(crate) const fn new(i: T, j: T) -> Self {
        Point { i, j }
    }
}

impl<T> ops::Add for Point<T>
where T: ops::Add<Output = T> {
    type Output = Self;

    fn add(self, other: Point<T>) -> Self::Output {
        Point::new(self.i + other.i, self.j + other.j)
    }
}

impl<T> ops::Add<T> for Point<T>
where T: ops::Add<T, Output = T> + Copy {
    type Output = Self;

    fn add(self, scalar: T) -> Self::Output {
        Point::new(self.i + scalar, self.j + scalar)
    }
}

impl<T> ops::Sub for Point<T>
where T: ops::Sub<Output = T> {
    type Output = Self;

    fn sub(self, other: Point<T>) -> Self::Output {
        Point::new(self.i - other.i, self.j - other.j)
    }
}

pub(crate) fn get_element<T, U>(matrix: &Vec<Vec<U>>, p: Point<T>) -> U
where T: TryInto<usize> + Copy, U: Copy {
    matrix[p.i.try_into().unwrap_or_default()][p.j.try_into().unwrap_or_default()]
}

pub(crate) fn set_element<T, U>(matrix: &mut Vec<Vec<U>>, p: Point<T>, c: U)
where T: TryInto<usize> + Copy {
    matrix[p.i.try_into().unwrap_or_default()][p.j.try_into().unwrap_or_default()] = c;
}

pub(crate) fn in_bounds(i: isize, j: isize, n_rows: usize, n_cols: usize) -> bool {
    i >= 0 && j >= 0 && (i as usize) < n_rows && (j as usize) < n_cols
}
