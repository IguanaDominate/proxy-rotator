from proxy_rotator.models.proxy import Proxy


def test_parse_plain_hostport() -> None:
    p = Proxy.parse("192.168.1.10:8080")
    assert p.host == "192.168.1.10"
    assert p.port == 8080
    assert p.protocol == "http"


def test_parse_with_scheme() -> None:
    p = Proxy.parse("socks5://10.0.0.1:1080")
    assert p.protocol == "socks5"
    assert p.as_url() == "socks5://10.0.0.1:1080"


def test_as_hostport() -> None:
    assert Proxy(host="1.2.3.4", port=80).as_hostport() == "1.2.3.4:80"