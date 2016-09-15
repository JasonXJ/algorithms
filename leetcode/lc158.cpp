#include <cassert>

// Forward declaration of the read4 API.
int read4(char *buf);


class Solution {
    static const int CHUNK_SIZE = 4;
    char cache[CHUNK_SIZE];
    int cache_size;
public:
    Solution(): cache_size(0) {}

    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        // Copy content in `cache`
        int copy_cache_count = cache_size;
        if (copy_cache_count > n)
            copy_cache_count = n;
        for (int i = 0; i < copy_cache_count; ++i) {
            buf[i] = cache[i];
        }
        shift_cache(copy_cache_count);
        int buf_size = copy_cache_count;
        if (buf_size == n) {
            return buf_size;
        }

        // Read from read4
        int read4_rv;
        while (buf_size <= n - 4) {
            read4_rv = read4(buf + buf_size);
            buf_size += read4_rv;
            if (read4_rv < CHUNK_SIZE)
                return buf_size;
        }

        // Reaching here means that n - 4 < buf_size <= n; if buf_size
        // < n, we need to read one more time.
        if (buf_size < n) {
            // Note that if we reach here, the cache must be empty already.
            assert(cache_size == 0);
            cache_size = read4(cache);
            int to_copy = cache_size;
            if (to_copy + buf_size > n) {
                to_copy = n - buf_size;
            }
            for (int i = 0, j = buf_size; i < to_copy; ++i, ++j) {
                buf[j] = cache[i];
            }
            buf_size += to_copy;
            shift_cache(to_copy);
        }
        return buf_size;
    }

    void shift_cache(int n) {
        if (n < cache_size) {
            for (int i = 0, j = n; j < cache_size; ++i, ++j)
                cache[i] = cache[j];
            cache_size -= n;
        } else {
            cache_size = 0;
        }

    }
};


#include <iostream>
using namespace std;

const char gbuf[] = "abcdefg";
const int BUF_SIZE = sizeof(gbuf) / sizeof(*gbuf) - 1;
int gindex = 0;

int read4(char *buf) {
    if (gindex > BUF_SIZE) {
        cout << "read4: 0" << endl;
        return 0;
    }
    int i = 0;
    cout << "read4: " << gindex;
    while (gindex < BUF_SIZE && i < 4) {
        buf[i++] = gbuf[gindex++];
    }
    cout << " -> " << gindex << " (" << i << ")" << endl;
    return i;
}


void fill_zero(char buf[10]) {
    for (int i = 0; i < 10; ++i) {
        buf[i] = '\0';
    }
}


int main(void)
{
    char buf[10];
    fill_zero(buf);
    //read4(buf);
    //cout << buf << endl;
    //read4(buf);
    //cout << buf << endl;
    //read4(buf);
    //cout << buf << endl;
    Solution s;
    cout << s.read(buf, 1) << endl;
    cout << buf << endl;
    cout << s.read(buf, 1) << endl;
    cout << buf << endl;
    cout << s.read(buf, 1) << endl;
    cout << buf << endl;
    cout << s.read(buf, 1) << endl;
    cout << buf << endl;
    cout << s.read(buf, 1) << endl;
    cout << buf << endl;
    cout << s.read(buf, 1) << endl;
    cout << buf << endl;
    cout << s.read(buf, 1) << endl;
    cout << buf << endl;
    cout << s.read(buf, 1) << endl;
    cout << buf << endl;
    cout << s.read(buf, 1) << endl;
    cout << buf << endl;
    cout << s.read(buf, 1) << endl;
    cout << buf << endl;
    //cout << s.read(buf, 6) << endl;
    //cout << buf << endl; fill_zero(buf);
    //cout << s.read(buf, 1) << endl;
    //cout << buf << endl; fill_zero(buf);
    //cout << s.read(buf, 1) << endl;
    //cout << buf << endl; fill_zero(buf);
    //cout << s.read(buf, 1) << endl;
    //cout << buf << endl; fill_zero(buf);

    
    return 0;
}
