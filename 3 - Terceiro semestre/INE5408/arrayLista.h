#ifndef STRUCTURES_ARRAY_LIST_H
#define STRUCTURES_ARRAY_LIST_H

#include <cstdint>


namespace structures {

template<typename T>
class ArrayList {
public:
    ArrayList();
    explicit ArrayList(std::size_t max_size);
    ~ArrayList();

    void clear();
    void push_back(const T& data);
    void push_front(const T& data);
    void insert(const T& data, std::size_t index);
    void insert_sorted(const T& data);
    T pop(std::size_t index);
    T pop_back();
    T pop_front();
    void remove(const T& data);
    bool full() const;
    bool empty() const;
    bool contains(const T& data) const;
    std::size_t find(const T& data) const;
    std::size_t size() const;
    std::size_t max_size() const;
    T& at(std::size_t index);
    T& operator[](std::size_t index);
    const T& at(std::size_t index) const;
    const T& operator[](std::size_t index) const;
    // descricao do 'operator []' na FAQ da disciplina

private:
    T* contents;
    std::size_t size_;
    std::size_t max_size_;
    static const auto DEFAULT_MAX = 10u;
};

}

#endif

template<typename T>
ArrayList<T>::ArrayList() {
    size_ = 0;
    max_size_ = DEFAULT_MAX;
    contents = new T[max_size_];
}

template<typename T>
ArrayList<T>::ArrayList(std::size_t max_size) {
    size_ = 0;
    max_size_ = max_size;
    contents = new T[max_size_];
}

template<typename T>
ArrayList<T>::~ArrayList() {
    delete[] contents;
}

template<typename T>
ArrayList<T>::clear() {
    size = 0;
}

template<typename T>
ArrayList<T>::push_back(const T& data) {
    insert(data, size_);
}

template<typename T>
ArrayList<T>::push_front(const T& data) {
    insert(data, 0);
}

template<typename T>
void ArrayList<T>::insert(const T& data, std::size_t index) {
    if (full()) {
        throw std::out_of_range("Lista cheia");
    } 
    
    if (index > size_) {
        throw std::out_of_range("Índice inválido");
    }

    for (int i = size_; i > index-1; i--) {
        contents[i + 1] = contents[i]
    }

    contents[index] = data;
    size_++;
}

template<typename T>
void ArrayList<T>::insert_sorted(const T& data) {
    if (full()) {
        throw std::out_of_range("Lista cheia");
    }

    if (index > size_) {
        throw std::out_of_range("Índice inválido");
    }

    for (auto i = size_; i > index; --i) {
        contents[i] = contents[i - 1];
    }

    for (int i = 0; i < size_; i++) {
        if (data < contents[i]) {
            insert(data, i-1);
            break;
        }
    }

template<typename T>
void ArrayList<T>::pop(std::size_t index) {
    if (empty()) {
        throw std::out_of_range("Lista vazia");
    }

    if (index >= size_) {
        throw std::out_of_range("Índice inválido");
    } 
    auto aux = contents[index];

    for (int i = index; i < size_ - 1; i++) {
        
    }
    }
}