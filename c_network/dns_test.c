#ifdef LINUX
#include <netdb.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
#include <errno.h>
#elif WIN32
#include <winsock2.h>
#endif
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <error.h>

int open_tcp_connect(const struct in_addr *addr)
{
    struct sockaddr_in serve;
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if(sock < 0)
    {
       perror("open_tcp_connect crean socket ");
       return -1;
    }
    memset(&serve,0, sizeof(serve));
    serve.sin_family = AF_INET;
    serve.sin_addr.s_addr = addr->s_addr;//inet_addr("127.0.0.1");
    serve.sin_port = htons(80);
    if(connect(sock, (struct sockaddr *)&serve, sizeof(serve)) < 0)
    {
        perror("open_tcp_connect connect ");
        printf("errno = %d\n", errno);
        return (errno == 115)?sock:-1;
    }
    return sock;
}

int http_get(int sock, const char *host)
{
    char buff[1024] = {'\0'};
    int n = 0;
    FILE *fp = fopen("./test.html", "w");
    sprintf(buff, "GET / HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n", host);
    send(sock, buff, strlen(buff), 0);
    n = recv(sock, buff, 1024, 0);
    char *data = strstr(buff, "\r\n\r\n");
    fwrite(data+4, strlen(data), 1, fp);
    while((n = recv(sock, buff, 1024, 0)) > 0)
    {
        
        fwrite(buff, n, 1, fp);
    }
    fclose(fp);
    return 0;
}

int close_tcp_connect(int sock)
{
    close(sock);
}

int main(int argc, char *argv[])
{
    char **pp;
    struct in_addr addr;
    struct hostent *p_host;
    int sock;
    p_host = gethostbyname(argv[1]?argv[1]:"www.baidu.com");
    printf("alias: %s\n", p_host->h_name);
    for(pp = p_host->h_addr_list; *pp != NULL;pp++)
    {
        printf("address:%s\n", inet_ntoa(*((struct in_addr*)*pp)));
        addr.s_addr = ((struct in_addr*)*pp)->s_addr;
        sock = open_tcp_connect(&addr);
        if(sock < 0)
            continue;
        http_get(sock, argv[1]?argv[1]:"www.baidu.com");
        if(sock)
        {
            close_tcp_connect(sock);
            break;
        }
    }
    return 0;
}
