Name:           curl
Version:	7.70.0
Release:        1%{?dist}
Summary:	A Client that groks URLs

License:	MIT
URL:		https://curl.haxx.se/
Source0:	https://curl.haxx.se/download/curl-%{version}.tar.gz

#BuildRequires:
#Requires:

%description

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
/usr/bin/curl
/usr/bin/curl-config
/usr/include/curl/curl.h
/usr/include/curl/curlver.h
/usr/include/curl/easy.h
/usr/include/curl/mprintf.h
/usr/include/curl/multi.h
/usr/include/curl/stdcheaders.h
/usr/include/curl/system.h
/usr/include/curl/typecheck-gcc.h
/usr/include/curl/urlapi.h
/usr/lib64/libcurl.a
/usr/lib64/libcurl.la
/usr/lib64/libcurl.so
/usr/lib64/libcurl.so.4
/usr/lib64/libcurl.so.4.6.0
/usr/lib64/pkgconfig/libcurl.pc
/usr/share/aclocal/libcurl.m4
/usr/share/man/man1/curl-config.1.gz
/usr/share/man/man1/curl.1.gz
/usr/share/man/man3/CURLINFO_ACTIVESOCKET.3.gz
/usr/share/man/man3/CURLINFO_APPCONNECT_TIME.3.gz
/usr/share/man/man3/CURLINFO_APPCONNECT_TIME_T.3.gz
/usr/share/man/man3/CURLINFO_CERTINFO.3.gz
/usr/share/man/man3/CURLINFO_CONDITION_UNMET.3.gz
/usr/share/man/man3/CURLINFO_CONNECT_TIME.3.gz
/usr/share/man/man3/CURLINFO_CONNECT_TIME_T.3.gz
/usr/share/man/man3/CURLINFO_CONTENT_LENGTH_DOWNLOAD.3.gz
/usr/share/man/man3/CURLINFO_CONTENT_LENGTH_DOWNLOAD_T.3.gz
/usr/share/man/man3/CURLINFO_CONTENT_LENGTH_UPLOAD.3.gz
/usr/share/man/man3/CURLINFO_CONTENT_LENGTH_UPLOAD_T.3.gz
/usr/share/man/man3/CURLINFO_CONTENT_TYPE.3.gz
/usr/share/man/man3/CURLINFO_COOKIELIST.3.gz
/usr/share/man/man3/CURLINFO_EFFECTIVE_URL.3.gz
/usr/share/man/man3/CURLINFO_FILETIME.3.gz
/usr/share/man/man3/CURLINFO_FILETIME_T.3.gz
/usr/share/man/man3/CURLINFO_FTP_ENTRY_PATH.3.gz
/usr/share/man/man3/CURLINFO_HEADER_SIZE.3.gz
/usr/share/man/man3/CURLINFO_HTTPAUTH_AVAIL.3.gz
/usr/share/man/man3/CURLINFO_HTTP_CONNECTCODE.3.gz
/usr/share/man/man3/CURLINFO_HTTP_VERSION.3.gz
/usr/share/man/man3/CURLINFO_LASTSOCKET.3.gz
/usr/share/man/man3/CURLINFO_LOCAL_IP.3.gz
/usr/share/man/man3/CURLINFO_LOCAL_PORT.3.gz
/usr/share/man/man3/CURLINFO_NAMELOOKUP_TIME.3.gz
/usr/share/man/man3/CURLINFO_NAMELOOKUP_TIME_T.3.gz
/usr/share/man/man3/CURLINFO_NUM_CONNECTS.3.gz
/usr/share/man/man3/CURLINFO_OS_ERRNO.3.gz
/usr/share/man/man3/CURLINFO_PRETRANSFER_TIME.3.gz
/usr/share/man/man3/CURLINFO_PRETRANSFER_TIME_T.3.gz
/usr/share/man/man3/CURLINFO_PRIMARY_IP.3.gz
/usr/share/man/man3/CURLINFO_PRIMARY_PORT.3.gz
/usr/share/man/man3/CURLINFO_PRIVATE.3.gz
/usr/share/man/man3/CURLINFO_PROTOCOL.3.gz
/usr/share/man/man3/CURLINFO_PROXYAUTH_AVAIL.3.gz
/usr/share/man/man3/CURLINFO_PROXY_SSL_VERIFYRESULT.3.gz
/usr/share/man/man3/CURLINFO_REDIRECT_COUNT.3.gz
/usr/share/man/man3/CURLINFO_REDIRECT_TIME.3.gz
/usr/share/man/man3/CURLINFO_REDIRECT_TIME_T.3.gz
/usr/share/man/man3/CURLINFO_REDIRECT_URL.3.gz
/usr/share/man/man3/CURLINFO_REQUEST_SIZE.3.gz
/usr/share/man/man3/CURLINFO_RESPONSE_CODE.3.gz
/usr/share/man/man3/CURLINFO_RETRY_AFTER.3.gz
/usr/share/man/man3/CURLINFO_RTSP_CLIENT_CSEQ.3.gz
/usr/share/man/man3/CURLINFO_RTSP_CSEQ_RECV.3.gz
/usr/share/man/man3/CURLINFO_RTSP_SERVER_CSEQ.3.gz
/usr/share/man/man3/CURLINFO_RTSP_SESSION_ID.3.gz
/usr/share/man/man3/CURLINFO_SCHEME.3.gz
/usr/share/man/man3/CURLINFO_SIZE_DOWNLOAD.3.gz
/usr/share/man/man3/CURLINFO_SIZE_DOWNLOAD_T.3.gz
/usr/share/man/man3/CURLINFO_SIZE_UPLOAD.3.gz
/usr/share/man/man3/CURLINFO_SIZE_UPLOAD_T.3.gz
/usr/share/man/man3/CURLINFO_SPEED_DOWNLOAD.3.gz
/usr/share/man/man3/CURLINFO_SPEED_DOWNLOAD_T.3.gz
/usr/share/man/man3/CURLINFO_SPEED_UPLOAD.3.gz
/usr/share/man/man3/CURLINFO_SPEED_UPLOAD_T.3.gz
/usr/share/man/man3/CURLINFO_SSL_ENGINES.3.gz
/usr/share/man/man3/CURLINFO_SSL_VERIFYRESULT.3.gz
/usr/share/man/man3/CURLINFO_STARTTRANSFER_TIME.3.gz
/usr/share/man/man3/CURLINFO_STARTTRANSFER_TIME_T.3.gz
/usr/share/man/man3/CURLINFO_TLS_SESSION.3.gz
/usr/share/man/man3/CURLINFO_TLS_SSL_PTR.3.gz
/usr/share/man/man3/CURLINFO_TOTAL_TIME.3.gz
/usr/share/man/man3/CURLINFO_TOTAL_TIME_T.3.gz
/usr/share/man/man3/CURLMOPT_CHUNK_LENGTH_PENALTY_SIZE.3.gz
/usr/share/man/man3/CURLMOPT_CONTENT_LENGTH_PENALTY_SIZE.3.gz
/usr/share/man/man3/CURLMOPT_MAXCONNECTS.3.gz
/usr/share/man/man3/CURLMOPT_MAX_CONCURRENT_STREAMS.3.gz
/usr/share/man/man3/CURLMOPT_MAX_HOST_CONNECTIONS.3.gz
/usr/share/man/man3/CURLMOPT_MAX_PIPELINE_LENGTH.3.gz
/usr/share/man/man3/CURLMOPT_MAX_TOTAL_CONNECTIONS.3.gz
/usr/share/man/man3/CURLMOPT_PIPELINING.3.gz
/usr/share/man/man3/CURLMOPT_PIPELINING_SERVER_BL.3.gz
/usr/share/man/man3/CURLMOPT_PIPELINING_SITE_BL.3.gz
/usr/share/man/man3/CURLMOPT_PUSHDATA.3.gz
/usr/share/man/man3/CURLMOPT_PUSHFUNCTION.3.gz
/usr/share/man/man3/CURLMOPT_SOCKETDATA.3.gz
/usr/share/man/man3/CURLMOPT_SOCKETFUNCTION.3.gz
/usr/share/man/man3/CURLMOPT_TIMERDATA.3.gz
/usr/share/man/man3/CURLMOPT_TIMERFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_ABSTRACT_UNIX_SOCKET.3.gz
/usr/share/man/man3/CURLOPT_ACCEPTTIMEOUT_MS.3.gz
/usr/share/man/man3/CURLOPT_ACCEPT_ENCODING.3.gz
/usr/share/man/man3/CURLOPT_ADDRESS_SCOPE.3.gz
/usr/share/man/man3/CURLOPT_ALTSVC.3.gz
/usr/share/man/man3/CURLOPT_ALTSVC_CTRL.3.gz
/usr/share/man/man3/CURLOPT_APPEND.3.gz
/usr/share/man/man3/CURLOPT_AUTOREFERER.3.gz
/usr/share/man/man3/CURLOPT_BUFFERSIZE.3.gz
/usr/share/man/man3/CURLOPT_CAINFO.3.gz
/usr/share/man/man3/CURLOPT_CAPATH.3.gz
/usr/share/man/man3/CURLOPT_CERTINFO.3.gz
/usr/share/man/man3/CURLOPT_CHUNK_BGN_FUNCTION.3.gz
/usr/share/man/man3/CURLOPT_CHUNK_DATA.3.gz
/usr/share/man/man3/CURLOPT_CHUNK_END_FUNCTION.3.gz
/usr/share/man/man3/CURLOPT_CLOSESOCKETDATA.3.gz
/usr/share/man/man3/CURLOPT_CLOSESOCKETFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_CONNECTTIMEOUT.3.gz
/usr/share/man/man3/CURLOPT_CONNECTTIMEOUT_MS.3.gz
/usr/share/man/man3/CURLOPT_CONNECT_ONLY.3.gz
/usr/share/man/man3/CURLOPT_CONNECT_TO.3.gz
/usr/share/man/man3/CURLOPT_CONV_FROM_NETWORK_FUNCTION.3.gz
/usr/share/man/man3/CURLOPT_CONV_FROM_UTF8_FUNCTION.3.gz
/usr/share/man/man3/CURLOPT_CONV_TO_NETWORK_FUNCTION.3.gz
/usr/share/man/man3/CURLOPT_COOKIE.3.gz
/usr/share/man/man3/CURLOPT_COOKIEFILE.3.gz
/usr/share/man/man3/CURLOPT_COOKIEJAR.3.gz
/usr/share/man/man3/CURLOPT_COOKIELIST.3.gz
/usr/share/man/man3/CURLOPT_COOKIESESSION.3.gz
/usr/share/man/man3/CURLOPT_COPYPOSTFIELDS.3.gz
/usr/share/man/man3/CURLOPT_CRLF.3.gz
/usr/share/man/man3/CURLOPT_CRLFILE.3.gz
/usr/share/man/man3/CURLOPT_CURLU.3.gz
/usr/share/man/man3/CURLOPT_CUSTOMREQUEST.3.gz
/usr/share/man/man3/CURLOPT_DEBUGDATA.3.gz
/usr/share/man/man3/CURLOPT_DEBUGFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_DEFAULT_PROTOCOL.3.gz
/usr/share/man/man3/CURLOPT_DIRLISTONLY.3.gz
/usr/share/man/man3/CURLOPT_DISALLOW_USERNAME_IN_URL.3.gz
/usr/share/man/man3/CURLOPT_DNS_CACHE_TIMEOUT.3.gz
/usr/share/man/man3/CURLOPT_DNS_INTERFACE.3.gz
/usr/share/man/man3/CURLOPT_DNS_LOCAL_IP4.3.gz
/usr/share/man/man3/CURLOPT_DNS_LOCAL_IP6.3.gz
/usr/share/man/man3/CURLOPT_DNS_SERVERS.3.gz
/usr/share/man/man3/CURLOPT_DNS_SHUFFLE_ADDRESSES.3.gz
/usr/share/man/man3/CURLOPT_DNS_USE_GLOBAL_CACHE.3.gz
/usr/share/man/man3/CURLOPT_DOH_URL.3.gz
/usr/share/man/man3/CURLOPT_EGDSOCKET.3.gz
/usr/share/man/man3/CURLOPT_ERRORBUFFER.3.gz
/usr/share/man/man3/CURLOPT_EXPECT_100_TIMEOUT_MS.3.gz
/usr/share/man/man3/CURLOPT_FAILONERROR.3.gz
/usr/share/man/man3/CURLOPT_FILETIME.3.gz
/usr/share/man/man3/CURLOPT_FNMATCH_DATA.3.gz
/usr/share/man/man3/CURLOPT_FNMATCH_FUNCTION.3.gz
/usr/share/man/man3/CURLOPT_FOLLOWLOCATION.3.gz
/usr/share/man/man3/CURLOPT_FORBID_REUSE.3.gz
/usr/share/man/man3/CURLOPT_FRESH_CONNECT.3.gz
/usr/share/man/man3/CURLOPT_FTPPORT.3.gz
/usr/share/man/man3/CURLOPT_FTPSSLAUTH.3.gz
/usr/share/man/man3/CURLOPT_FTP_ACCOUNT.3.gz
/usr/share/man/man3/CURLOPT_FTP_ALTERNATIVE_TO_USER.3.gz
/usr/share/man/man3/CURLOPT_FTP_CREATE_MISSING_DIRS.3.gz
/usr/share/man/man3/CURLOPT_FTP_FILEMETHOD.3.gz
/usr/share/man/man3/CURLOPT_FTP_RESPONSE_TIMEOUT.3.gz
/usr/share/man/man3/CURLOPT_FTP_SKIP_PASV_IP.3.gz
/usr/share/man/man3/CURLOPT_FTP_SSL_CCC.3.gz
/usr/share/man/man3/CURLOPT_FTP_USE_EPRT.3.gz
/usr/share/man/man3/CURLOPT_FTP_USE_EPSV.3.gz
/usr/share/man/man3/CURLOPT_FTP_USE_PRET.3.gz
/usr/share/man/man3/CURLOPT_GSSAPI_DELEGATION.3.gz
/usr/share/man/man3/CURLOPT_HAPPY_EYEBALLS_TIMEOUT_MS.3.gz
/usr/share/man/man3/CURLOPT_HAPROXYPROTOCOL.3.gz
/usr/share/man/man3/CURLOPT_HEADER.3.gz
/usr/share/man/man3/CURLOPT_HEADERDATA.3.gz
/usr/share/man/man3/CURLOPT_HEADERFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_HEADEROPT.3.gz
/usr/share/man/man3/CURLOPT_HTTP09_ALLOWED.3.gz
/usr/share/man/man3/CURLOPT_HTTP200ALIASES.3.gz
/usr/share/man/man3/CURLOPT_HTTPAUTH.3.gz
/usr/share/man/man3/CURLOPT_HTTPGET.3.gz
/usr/share/man/man3/CURLOPT_HTTPHEADER.3.gz
/usr/share/man/man3/CURLOPT_HTTPPOST.3.gz
/usr/share/man/man3/CURLOPT_HTTPPROXYTUNNEL.3.gz
/usr/share/man/man3/CURLOPT_HTTP_CONTENT_DECODING.3.gz
/usr/share/man/man3/CURLOPT_HTTP_TRANSFER_DECODING.3.gz
/usr/share/man/man3/CURLOPT_HTTP_VERSION.3.gz
/usr/share/man/man3/CURLOPT_IGNORE_CONTENT_LENGTH.3.gz
/usr/share/man/man3/CURLOPT_INFILESIZE.3.gz
/usr/share/man/man3/CURLOPT_INFILESIZE_LARGE.3.gz
/usr/share/man/man3/CURLOPT_INTERFACE.3.gz
/usr/share/man/man3/CURLOPT_INTERLEAVEDATA.3.gz
/usr/share/man/man3/CURLOPT_INTERLEAVEFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_IOCTLDATA.3.gz
/usr/share/man/man3/CURLOPT_IOCTLFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_IPRESOLVE.3.gz
/usr/share/man/man3/CURLOPT_ISSUERCERT.3.gz
/usr/share/man/man3/CURLOPT_KEEP_SENDING_ON_ERROR.3.gz
/usr/share/man/man3/CURLOPT_KEYPASSWD.3.gz
/usr/share/man/man3/CURLOPT_KRBLEVEL.3.gz
/usr/share/man/man3/CURLOPT_LOCALPORT.3.gz
/usr/share/man/man3/CURLOPT_LOCALPORTRANGE.3.gz
/usr/share/man/man3/CURLOPT_LOGIN_OPTIONS.3.gz
/usr/share/man/man3/CURLOPT_LOW_SPEED_LIMIT.3.gz
/usr/share/man/man3/CURLOPT_LOW_SPEED_TIME.3.gz
/usr/share/man/man3/CURLOPT_MAIL_AUTH.3.gz
/usr/share/man/man3/CURLOPT_MAIL_FROM.3.gz
/usr/share/man/man3/CURLOPT_MAIL_RCPT.3.gz
/usr/share/man/man3/CURLOPT_MAIL_RCPT_ALLLOWFAILS.3.gz
/usr/share/man/man3/CURLOPT_MAXAGE_CONN.3.gz
/usr/share/man/man3/CURLOPT_MAXCONNECTS.3.gz
/usr/share/man/man3/CURLOPT_MAXFILESIZE.3.gz
/usr/share/man/man3/CURLOPT_MAXFILESIZE_LARGE.3.gz
/usr/share/man/man3/CURLOPT_MAXREDIRS.3.gz
/usr/share/man/man3/CURLOPT_MAX_RECV_SPEED_LARGE.3.gz
/usr/share/man/man3/CURLOPT_MAX_SEND_SPEED_LARGE.3.gz
/usr/share/man/man3/CURLOPT_MIMEPOST.3.gz
/usr/share/man/man3/CURLOPT_NETRC.3.gz
/usr/share/man/man3/CURLOPT_NETRC_FILE.3.gz
/usr/share/man/man3/CURLOPT_NEW_DIRECTORY_PERMS.3.gz
/usr/share/man/man3/CURLOPT_NEW_FILE_PERMS.3.gz
/usr/share/man/man3/CURLOPT_NOBODY.3.gz
/usr/share/man/man3/CURLOPT_NOPROGRESS.3.gz
/usr/share/man/man3/CURLOPT_NOPROXY.3.gz
/usr/share/man/man3/CURLOPT_NOSIGNAL.3.gz
/usr/share/man/man3/CURLOPT_OPENSOCKETDATA.3.gz
/usr/share/man/man3/CURLOPT_OPENSOCKETFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_PASSWORD.3.gz
/usr/share/man/man3/CURLOPT_PATH_AS_IS.3.gz
/usr/share/man/man3/CURLOPT_PINNEDPUBLICKEY.3.gz
/usr/share/man/man3/CURLOPT_PIPEWAIT.3.gz
/usr/share/man/man3/CURLOPT_PORT.3.gz
/usr/share/man/man3/CURLOPT_POST.3.gz
/usr/share/man/man3/CURLOPT_POSTFIELDS.3.gz
/usr/share/man/man3/CURLOPT_POSTFIELDSIZE.3.gz
/usr/share/man/man3/CURLOPT_POSTFIELDSIZE_LARGE.3.gz
/usr/share/man/man3/CURLOPT_POSTQUOTE.3.gz
/usr/share/man/man3/CURLOPT_POSTREDIR.3.gz
/usr/share/man/man3/CURLOPT_PREQUOTE.3.gz
/usr/share/man/man3/CURLOPT_PRE_PROXY.3.gz
/usr/share/man/man3/CURLOPT_PRIVATE.3.gz
/usr/share/man/man3/CURLOPT_PROGRESSDATA.3.gz
/usr/share/man/man3/CURLOPT_PROGRESSFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_PROTOCOLS.3.gz
/usr/share/man/man3/CURLOPT_PROXY.3.gz
/usr/share/man/man3/CURLOPT_PROXYAUTH.3.gz
/usr/share/man/man3/CURLOPT_PROXYHEADER.3.gz
/usr/share/man/man3/CURLOPT_PROXYPASSWORD.3.gz
/usr/share/man/man3/CURLOPT_PROXYPORT.3.gz
/usr/share/man/man3/CURLOPT_PROXYTYPE.3.gz
/usr/share/man/man3/CURLOPT_PROXYUSERNAME.3.gz
/usr/share/man/man3/CURLOPT_PROXYUSERPWD.3.gz
/usr/share/man/man3/CURLOPT_PROXY_CAINFO.3.gz
/usr/share/man/man3/CURLOPT_PROXY_CAPATH.3.gz
/usr/share/man/man3/CURLOPT_PROXY_CRLFILE.3.gz
/usr/share/man/man3/CURLOPT_PROXY_KEYPASSWD.3.gz
/usr/share/man/man3/CURLOPT_PROXY_PINNEDPUBLICKEY.3.gz
/usr/share/man/man3/CURLOPT_PROXY_SERVICE_NAME.3.gz
/usr/share/man/man3/CURLOPT_PROXY_SSLCERT.3.gz
/usr/share/man/man3/CURLOPT_PROXY_SSLCERTTYPE.3.gz
/usr/share/man/man3/CURLOPT_PROXY_SSLKEY.3.gz
/usr/share/man/man3/CURLOPT_PROXY_SSLKEYTYPE.3.gz
/usr/share/man/man3/CURLOPT_PROXY_SSLVERSION.3.gz
/usr/share/man/man3/CURLOPT_PROXY_SSL_CIPHER_LIST.3.gz
/usr/share/man/man3/CURLOPT_PROXY_SSL_OPTIONS.3.gz
/usr/share/man/man3/CURLOPT_PROXY_SSL_VERIFYHOST.3.gz
/usr/share/man/man3/CURLOPT_PROXY_SSL_VERIFYPEER.3.gz
/usr/share/man/man3/CURLOPT_PROXY_TLS13_CIPHERS.3.gz
/usr/share/man/man3/CURLOPT_PROXY_TLSAUTH_PASSWORD.3.gz
/usr/share/man/man3/CURLOPT_PROXY_TLSAUTH_TYPE.3.gz
/usr/share/man/man3/CURLOPT_PROXY_TLSAUTH_USERNAME.3.gz
/usr/share/man/man3/CURLOPT_PROXY_TRANSFER_MODE.3.gz
/usr/share/man/man3/CURLOPT_PUT.3.gz
/usr/share/man/man3/CURLOPT_QUOTE.3.gz
/usr/share/man/man3/CURLOPT_RANDOM_FILE.3.gz
/usr/share/man/man3/CURLOPT_RANGE.3.gz
/usr/share/man/man3/CURLOPT_READDATA.3.gz
/usr/share/man/man3/CURLOPT_READFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_REDIR_PROTOCOLS.3.gz
/usr/share/man/man3/CURLOPT_REFERER.3.gz
/usr/share/man/man3/CURLOPT_REQUEST_TARGET.3.gz
/usr/share/man/man3/CURLOPT_RESOLVE.3.gz
/usr/share/man/man3/CURLOPT_RESOLVER_START_DATA.3.gz
/usr/share/man/man3/CURLOPT_RESOLVER_START_FUNCTION.3.gz
/usr/share/man/man3/CURLOPT_RESUME_FROM.3.gz
/usr/share/man/man3/CURLOPT_RESUME_FROM_LARGE.3.gz
/usr/share/man/man3/CURLOPT_RTSP_CLIENT_CSEQ.3.gz
/usr/share/man/man3/CURLOPT_RTSP_REQUEST.3.gz
/usr/share/man/man3/CURLOPT_RTSP_SERVER_CSEQ.3.gz
/usr/share/man/man3/CURLOPT_RTSP_SESSION_ID.3.gz
/usr/share/man/man3/CURLOPT_RTSP_STREAM_URI.3.gz
/usr/share/man/man3/CURLOPT_RTSP_TRANSPORT.3.gz
/usr/share/man/man3/CURLOPT_SASL_AUTHZID.3.gz
/usr/share/man/man3/CURLOPT_SASL_IR.3.gz
/usr/share/man/man3/CURLOPT_SEEKDATA.3.gz
/usr/share/man/man3/CURLOPT_SEEKFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_SERVICE_NAME.3.gz
/usr/share/man/man3/CURLOPT_SHARE.3.gz
/usr/share/man/man3/CURLOPT_SOCKOPTDATA.3.gz
/usr/share/man/man3/CURLOPT_SOCKOPTFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_SOCKS5_AUTH.3.gz
/usr/share/man/man3/CURLOPT_SOCKS5_GSSAPI_NEC.3.gz
/usr/share/man/man3/CURLOPT_SOCKS5_GSSAPI_SERVICE.3.gz
/usr/share/man/man3/CURLOPT_SSH_AUTH_TYPES.3.gz
/usr/share/man/man3/CURLOPT_SSH_COMPRESSION.3.gz
/usr/share/man/man3/CURLOPT_SSH_HOST_PUBLIC_KEY_MD5.3.gz
/usr/share/man/man3/CURLOPT_SSH_KEYDATA.3.gz
/usr/share/man/man3/CURLOPT_SSH_KEYFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_SSH_KNOWNHOSTS.3.gz
/usr/share/man/man3/CURLOPT_SSH_PRIVATE_KEYFILE.3.gz
/usr/share/man/man3/CURLOPT_SSH_PUBLIC_KEYFILE.3.gz
/usr/share/man/man3/CURLOPT_SSLCERT.3.gz
/usr/share/man/man3/CURLOPT_SSLCERTTYPE.3.gz
/usr/share/man/man3/CURLOPT_SSLENGINE.3.gz
/usr/share/man/man3/CURLOPT_SSLENGINE_DEFAULT.3.gz
/usr/share/man/man3/CURLOPT_SSLKEY.3.gz
/usr/share/man/man3/CURLOPT_SSLKEYTYPE.3.gz
/usr/share/man/man3/CURLOPT_SSLVERSION.3.gz
/usr/share/man/man3/CURLOPT_SSL_CIPHER_LIST.3.gz
/usr/share/man/man3/CURLOPT_SSL_CTX_DATA.3.gz
/usr/share/man/man3/CURLOPT_SSL_CTX_FUNCTION.3.gz
/usr/share/man/man3/CURLOPT_SSL_ENABLE_ALPN.3.gz
/usr/share/man/man3/CURLOPT_SSL_ENABLE_NPN.3.gz
/usr/share/man/man3/CURLOPT_SSL_FALSESTART.3.gz
/usr/share/man/man3/CURLOPT_SSL_OPTIONS.3.gz
/usr/share/man/man3/CURLOPT_SSL_SESSIONID_CACHE.3.gz
/usr/share/man/man3/CURLOPT_SSL_VERIFYHOST.3.gz
/usr/share/man/man3/CURLOPT_SSL_VERIFYPEER.3.gz
/usr/share/man/man3/CURLOPT_SSL_VERIFYSTATUS.3.gz
/usr/share/man/man3/CURLOPT_STDERR.3.gz
/usr/share/man/man3/CURLOPT_STREAM_DEPENDS.3.gz
/usr/share/man/man3/CURLOPT_STREAM_DEPENDS_E.3.gz
/usr/share/man/man3/CURLOPT_STREAM_WEIGHT.3.gz
/usr/share/man/man3/CURLOPT_SUPPRESS_CONNECT_HEADERS.3.gz
/usr/share/man/man3/CURLOPT_TCP_FASTOPEN.3.gz
/usr/share/man/man3/CURLOPT_TCP_KEEPALIVE.3.gz
/usr/share/man/man3/CURLOPT_TCP_KEEPIDLE.3.gz
/usr/share/man/man3/CURLOPT_TCP_KEEPINTVL.3.gz
/usr/share/man/man3/CURLOPT_TCP_NODELAY.3.gz
/usr/share/man/man3/CURLOPT_TELNETOPTIONS.3.gz
/usr/share/man/man3/CURLOPT_TFTP_BLKSIZE.3.gz
/usr/share/man/man3/CURLOPT_TFTP_NO_OPTIONS.3.gz
/usr/share/man/man3/CURLOPT_TIMECONDITION.3.gz
/usr/share/man/man3/CURLOPT_TIMEOUT.3.gz
/usr/share/man/man3/CURLOPT_TIMEOUT_MS.3.gz
/usr/share/man/man3/CURLOPT_TIMEVALUE.3.gz
/usr/share/man/man3/CURLOPT_TIMEVALUE_LARGE.3.gz
/usr/share/man/man3/CURLOPT_TLS13_CIPHERS.3.gz
/usr/share/man/man3/CURLOPT_TLSAUTH_PASSWORD.3.gz
/usr/share/man/man3/CURLOPT_TLSAUTH_TYPE.3.gz
/usr/share/man/man3/CURLOPT_TLSAUTH_USERNAME.3.gz
/usr/share/man/man3/CURLOPT_TRAILERDATA.3.gz
/usr/share/man/man3/CURLOPT_TRAILERFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_TRANSFERTEXT.3.gz
/usr/share/man/man3/CURLOPT_TRANSFER_ENCODING.3.gz
/usr/share/man/man3/CURLOPT_UNIX_SOCKET_PATH.3.gz
/usr/share/man/man3/CURLOPT_UNRESTRICTED_AUTH.3.gz
/usr/share/man/man3/CURLOPT_UPKEEP_INTERVAL_MS.3.gz
/usr/share/man/man3/CURLOPT_UPLOAD.3.gz
/usr/share/man/man3/CURLOPT_UPLOAD_BUFFERSIZE.3.gz
/usr/share/man/man3/CURLOPT_URL.3.gz
/usr/share/man/man3/CURLOPT_USERAGENT.3.gz
/usr/share/man/man3/CURLOPT_USERNAME.3.gz
/usr/share/man/man3/CURLOPT_USERPWD.3.gz
/usr/share/man/man3/CURLOPT_USE_SSL.3.gz
/usr/share/man/man3/CURLOPT_VERBOSE.3.gz
/usr/share/man/man3/CURLOPT_WILDCARDMATCH.3.gz
/usr/share/man/man3/CURLOPT_WRITEDATA.3.gz
/usr/share/man/man3/CURLOPT_WRITEFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_XFERINFODATA.3.gz
/usr/share/man/man3/CURLOPT_XFERINFOFUNCTION.3.gz
/usr/share/man/man3/CURLOPT_XOAUTH2_BEARER.3.gz
/usr/share/man/man3/curl_easy_cleanup.3.gz
/usr/share/man/man3/curl_easy_duphandle.3.gz
/usr/share/man/man3/curl_easy_escape.3.gz
/usr/share/man/man3/curl_easy_getinfo.3.gz
/usr/share/man/man3/curl_easy_init.3.gz
/usr/share/man/man3/curl_easy_pause.3.gz
/usr/share/man/man3/curl_easy_perform.3.gz
/usr/share/man/man3/curl_easy_recv.3.gz
/usr/share/man/man3/curl_easy_reset.3.gz
/usr/share/man/man3/curl_easy_send.3.gz
/usr/share/man/man3/curl_easy_setopt.3.gz
/usr/share/man/man3/curl_easy_strerror.3.gz
/usr/share/man/man3/curl_easy_unescape.3.gz
/usr/share/man/man3/curl_easy_upkeep.3.gz
/usr/share/man/man3/curl_escape.3.gz
/usr/share/man/man3/curl_formadd.3.gz
/usr/share/man/man3/curl_formfree.3.gz
/usr/share/man/man3/curl_formget.3.gz
/usr/share/man/man3/curl_free.3.gz
/usr/share/man/man3/curl_getdate.3.gz
/usr/share/man/man3/curl_getenv.3.gz
/usr/share/man/man3/curl_global_cleanup.3.gz
/usr/share/man/man3/curl_global_init.3.gz
/usr/share/man/man3/curl_global_init_mem.3.gz
/usr/share/man/man3/curl_global_sslset.3.gz
/usr/share/man/man3/curl_mime_addpart.3.gz
/usr/share/man/man3/curl_mime_data.3.gz
/usr/share/man/man3/curl_mime_data_cb.3.gz
/usr/share/man/man3/curl_mime_encoder.3.gz
/usr/share/man/man3/curl_mime_filedata.3.gz
/usr/share/man/man3/curl_mime_filename.3.gz
/usr/share/man/man3/curl_mime_free.3.gz
/usr/share/man/man3/curl_mime_headers.3.gz
/usr/share/man/man3/curl_mime_init.3.gz
/usr/share/man/man3/curl_mime_name.3.gz
/usr/share/man/man3/curl_mime_subparts.3.gz
/usr/share/man/man3/curl_mime_type.3.gz
/usr/share/man/man3/curl_mprintf.3.gz
/usr/share/man/man3/curl_multi_add_handle.3.gz
/usr/share/man/man3/curl_multi_assign.3.gz
/usr/share/man/man3/curl_multi_cleanup.3.gz
/usr/share/man/man3/curl_multi_fdset.3.gz
/usr/share/man/man3/curl_multi_info_read.3.gz
/usr/share/man/man3/curl_multi_init.3.gz
/usr/share/man/man3/curl_multi_perform.3.gz
/usr/share/man/man3/curl_multi_poll.3.gz
/usr/share/man/man3/curl_multi_remove_handle.3.gz
/usr/share/man/man3/curl_multi_setopt.3.gz
/usr/share/man/man3/curl_multi_socket.3.gz
/usr/share/man/man3/curl_multi_socket_action.3.gz
/usr/share/man/man3/curl_multi_socket_all.3.gz
/usr/share/man/man3/curl_multi_strerror.3.gz
/usr/share/man/man3/curl_multi_timeout.3.gz
/usr/share/man/man3/curl_multi_wait.3.gz
/usr/share/man/man3/curl_multi_wakeup.3.gz
/usr/share/man/man3/curl_share_cleanup.3.gz
/usr/share/man/man3/curl_share_init.3.gz
/usr/share/man/man3/curl_share_setopt.3.gz
/usr/share/man/man3/curl_share_strerror.3.gz
/usr/share/man/man3/curl_slist_append.3.gz
/usr/share/man/man3/curl_slist_free_all.3.gz
/usr/share/man/man3/curl_strequal.3.gz
/usr/share/man/man3/curl_strnequal.3.gz
/usr/share/man/man3/curl_unescape.3.gz
/usr/share/man/man3/curl_url.3.gz
/usr/share/man/man3/curl_url_cleanup.3.gz
/usr/share/man/man3/curl_url_dup.3.gz
/usr/share/man/man3/curl_url_get.3.gz
/usr/share/man/man3/curl_url_set.3.gz
/usr/share/man/man3/curl_version.3.gz
/usr/share/man/man3/curl_version_info.3.gz
/usr/share/man/man3/libcurl-easy.3.gz
/usr/share/man/man3/libcurl-env.3.gz
/usr/share/man/man3/libcurl-errors.3.gz
/usr/share/man/man3/libcurl-multi.3.gz
/usr/share/man/man3/libcurl-security.3.gz
/usr/share/man/man3/libcurl-share.3.gz
/usr/share/man/man3/libcurl-symbols.3.gz
/usr/share/man/man3/libcurl-thread.3.gz
/usr/share/man/man3/libcurl-tutorial.3.gz
/usr/share/man/man3/libcurl-url.3.gz
/usr/share/man/man3/libcurl.3.gz


# see /usr/libexec/rpm/macros for macros
